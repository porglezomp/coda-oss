/* =========================================================================
 * This file is part of sys-c++ 
 * =========================================================================
 * 
 * (C) Copyright 2004 - 2009, General Dynamics - Advanced Information Systems
 *
 * sys-c++ is free software; you can redistribute it and/or modify
 * it under the terms of the GNU Lesser General Public License as published by
 * the Free Software Foundation; either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public 
 * License along with this program; If not, 
 * see <http://www.gnu.org/licenses/>.
 *
 */

#include "sys/UTCDateTime.h"

#include "sys/Conf.h"
#include "except/Exception.h"
#include "str/Convert.h"
#include "str/Manip.h"

#include <errno.h>


namespace
{

// These constants and functions were taken from the NRT DateTime.c implementation

const long UNIX_EPOCH_YEAR(1970); // EPOCH = Jan 1 1970 00:00:00
const double SECS_IN_MIN(60.0);
const double SECS_IN_HOUR(60.0 * SECS_IN_MIN);
const double SECS_IN_DAY(24.0 * SECS_IN_HOUR);

// At the end of each month, the total number of days so far in the year.
// Index 0 is for non-leap years, index 1 is for leap years
const int CUMULATIVE_DAYS_PER_MONTH[2][12] =
{
    {31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365},
    {31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 366}
};

// The number of days in a year.  Index 0 is for non-leap years, index 1 is
// for leap years
const int DAYS_PER_YEAR[2] = {365, 366};

// Returns the appropriate index into CUMULATIVE_DAYS_PER_MONTH based on
// whether 'year' is a leap year or not
int yearIndex(int year)
{
    return (!(year % 4) && ((year % 100) || !(year % 400)));
}

// Returns the # of full days so far in the year
// 'month' and 'dayOfMonth' are 1-based
// So, getNumFullDaysInYearSoFar(2000, 1, 1) = 0
//     getNumFullDaysInYearSoFar(2000, 1, 2) = 1
//     getNumFullDaysInYearSoFar(2000, 2, 1) = 31
int getNumFullDaysInYearSoFar(int year, int month, int dayOfMonth)
{
    /* The number of days for all the full months so far */
    int numFullDays = (month > 1) ?
        CUMULATIVE_DAYS_PER_MONTH[yearIndex(year)][month - 2] :
        0;

    /* The number of full days in this month so far */
    numFullDays += dayOfMonth - 1;
    return numFullDays;
}

}

const char sys::UTCDateTime::DEFAULT_DATETIME_FORMAT[] = "%Y-%m-%dT%H:%M:%SZ";


void sys::UTCDateTime::fromMillis()
{
    tm t;
    getTime(t);

    // this is year since 1900 so need to add that
    mYear = t.tm_year + 1900;
    // 0-based so add 1
    mMonth = t.tm_mon + 1;
    mDayOfMonth = t.tm_mday;
    mDayOfWeek = t.tm_wday + 1;
    mDayOfYear = t.tm_yday + 1;
    mHour = t.tm_hour;
    mMinute = t.tm_min;

    const size_t timeInSeconds = (mTimeInMillis / 1000);
    const double timediff = ((double)mTimeInMillis / 1000.0) - timeInSeconds;
    mSecond = t.tm_sec + timediff;
}

void sys::UTCDateTime::toMillis()
{
    if (mSecond < 0.0 || mSecond >= 60.0 ||
            mMinute < 0 || mMinute > 59 ||
            mHour < 0 || mHour > 23 ||
            mDayOfMonth < 1 || mDayOfMonth > 31 ||
            mMonth < 1 || mMonth > 12 ||
            mYear < 1970 || mYear > 2037)
    {
        mTimeInMillis = 0.0;
        mDayOfYear = mDayOfWeek = 0;
        return;
    }

    /* Essentially we are implementing a simplified variant of mktime() here.
     * Implementation loosely based on
     * http://www.raspberryginger.com/jbailey/minix/html/mktime_8c-source.html
     * The problem with mktime() is that it expects local time and we are in
     * GMT.  Note that we can't just call mktime(), then look at the
     * difference between localtime() and gmtime() and offset the result by
     * that amount because this approach can't reliably take daylight savings
     * time into account.  Another option would be to trick mktime() by
     * setting the TZ environment variable to UTC, but this wouldn't be
     * reentrant.
     * It is very unfortunate that there's no POSIX standard function similar
     * to mktime() that allows you to pass in the timezone you want.
     */
    long numDaysThisYear = getNumFullDaysInYearSoFar(mYear, mMonth, mDayOfMonth);
    long numDaysSinceEpoch = 0;

    /* Count up the # of days for all the years prior to this one
     * TODO: This could be implemented more efficiently - see reference
     * implementation above. */
    for (int i = UNIX_EPOCH_YEAR; i < mYear; ++i)
    {
        numDaysSinceEpoch += DAYS_PER_YEAR[yearIndex(i)];
    }
    numDaysSinceEpoch += numDaysThisYear;

    mTimeInMillis = (mSecond + mMinute * SECS_IN_MIN +
            mHour * SECS_IN_HOUR + numDaysSinceEpoch * SECS_IN_DAY) * 1000.0;
    mDayOfYear = numDaysThisYear + 1;
    
    /* January 1, 1970 was a Thursday (5) */
    mDayOfWeek = (numDaysSinceEpoch + 5) % 7;
}



void sys::UTCDateTime::getTime(tm &gmTime) const
{
    getTime(static_cast<time_t>(mTimeInMillis / 1000), gmTime);
}

sys::UTCDateTime::UTCDateTime()
{
    setNow();
    toMillis();
}

sys::UTCDateTime::UTCDateTime(int hour, int minute, double second)
{
    setNow();

    mHour = hour;
    mMinute = minute;
    mSecond = second;

    toMillis();
}

sys::UTCDateTime::UTCDateTime(int year, int month, int day)
{
    setNow();

    mYear = year;
    mMonth = month;
    mDayOfMonth = day;

    toMillis();
    fromMillis();
}

sys::UTCDateTime::UTCDateTime(int year, int month, int day,
                        int hour, int minute, double second)
{
    setNow();

    mYear = year;
    mMonth = month;
    mDayOfMonth = day;
    mHour = hour;
    mMinute = minute;
    mSecond = second;

    toMillis();
    fromMillis();
}

sys::UTCDateTime::UTCDateTime(double timeInMillis)
{
    mTimeInMillis = timeInMillis;

    fromMillis();
}


void sys::UTCDateTime::getTime(time_t numSecondsSinceEpoch, tm &gmTime)
{
    // Would like to use the reentrant version.  If we don't have one, cross
    // our fingers and hope the regular function actually is reentrant
    // (supposedly this is the case on Windows).
#ifdef HAVE_GMTIME_R
    if (::gmtime_r(&numSecondsSinceEpoch, &gmTime) == NULL)
    {
        int const errnum = errno;
        throw except::Exception(Ctxt("gmtime_r() failed (" +
            std::string(::strerror(errnum)) + ")"));
    }
#else
    tm const * const gmTimePtr = ::gmtime(&numSecondsSinceEpoch);
    if (gmTimePtr == NULL)
    {
        int const errnum = errno;
        throw except::Exception(Ctxt("gmtime failed (" +
            std::string(::strerror(errnum)) + ")"));
    }
    gmTime = *gmTimePtr;
#endif
}

std::string sys::UTCDateTime::format() const
{
    return DateTime::format(DEFAULT_DATETIME_FORMAT);
}

