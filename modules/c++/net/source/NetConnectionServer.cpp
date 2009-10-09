/* =========================================================================
 * This file is part of net-c++ 
 * =========================================================================
 * 
 * (C) Copyright 2004 - 2009, General Dynamics - Advanced Information Systems
 *
 * net-c++ is free software; you can redistribute it and/or modify
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

#include "net/NetConnectionServer.h"

net::NetConnectionServer::NetConnectionServer() :
        mPortNumber(0), mBacklog(0), mAllocStrategy(NULL)
{}

net::NetConnectionServer::~NetConnectionServer()
{
    setAllocStrategy(NULL);
}

void net::NetConnectionServer::create(int portNumber, int backlog)
{
    mPortNumber = portNumber;
    net::SocketAddress address(mPortNumber);
    TCPServerSocketFactory socketFactory(backlog);
    mSocket = socketFactory.create(address);
    //mSocket = TCPServerSocketFactory(backlog).create(address);
}

std::string net::NetConnectionServer::getHostName()
{
    char name[MAXHOSTNAMELEN + 1];
    ::gethostname(name, MAXHOSTNAMELEN + 1);
    return std::string(name);
}

net::NetConnection* net::NetConnectionServer::accept()
{
    net::SocketAddress sa;
    return new net::NetConnection(mSocket.accept(sa));
}

void net::NetConnectionServer::handleClients()
{
    while (true)
    {
        net::NetConnection* conn = accept();
        mAllocStrategy->handleConnection(conn);
    }
}

void net::NetConnectionServer::setAllocStrategy(net::AllocStrategy* newStrategy)
{
    if (mAllocStrategy != NULL)
        delete mAllocStrategy;
    mAllocStrategy = newStrategy;
}