/* =========================================================================
 * This file is part of mem-c++
 * =========================================================================
 *
 * (C) Copyright 2004 - 2014, MDA Information Systems LLC
 *
 * mem-c++ is free software; you can redistribute it and/or modify
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

#ifndef __MEM_SCOPED_CLONEABLE_PTR_H__
#define __MEM_SCOPED_CLONEABLE_PTR_H__

#include <memory>
#include <cstddef>

namespace mem
{
/*!
 *  \class ScopedCloneablePtr
 *  \brief This class provides RAII for object allocations via new.  It is a
 *         light wrapper around std::auto_ptr and has the same semantics
 *         except that the copy constructor and assignment operator are deep
 *         copies (by using T's clone() method) rather than transferring
 *         ownership.
 *
 *         This is useful for cases where you have a class which has a member
 *         variable that's dynamically allocated and you want to provide a
 *         valid copy constructor / assignment operator.  With raw pointers or
 *         std::auto_ptr's, you'll have to write the copy constructor /
 *         assignment operator for this class - this is tedious and
 *         error-prone since you need to include all the members in the class.
 *         Using ScopedCloneablePtr's instead, the compiler-generated copy
 *         constructor and assignment operator for your class will be correct
 *         (if all the other member variables are POD or have correct
 *         copy constructors / assignment operators).
 */
template <class T>
class ScopedCloneablePtr
{
public:
    explicit ScopedCloneablePtr(T* ptr = NULL)
    : mPtr(ptr)
    {
    }

    ScopedCloneablePtr(const ScopedCloneablePtr& rhs)
    {
        if (rhs.mPtr.get())
        {
            mPtr.reset(rhs.mPtr->clone());
        }
    }

    const ScopedCloneablePtr&
    operator=(const ScopedCloneablePtr& rhs)
    {
        if (this != &rhs)
        {
            if (rhs.mPtr.get())
            {
                mPtr.reset(rhs.mPtr->clone());
            }
            else
            {
                mPtr.reset();
            }
        }

        return *this;
    }

    T* get() const
    {
        return mPtr.get();
    }

    T& operator*() const
    {
        return *mPtr;
    }

    T* operator->() const
    {
        return mPtr.get();
    }

    void reset(T* ptr = NULL)
    {
        mPtr.reset(ptr);
    }

private:
    std::auto_ptr<T> mPtr;
};
}

#endif
