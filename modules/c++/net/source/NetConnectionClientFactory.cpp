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

#include "net/NetConnectionClientFactory.h"

namespace net
{
static net::HostEnt_T* getHostByName(const std::string& hostname)
{
    return gethostbyname(hostname.c_str());
}
}

net::NetConnection *net::NetConnectionClientFactory::create(const net::URL& url)
{
    net::HostEnt_T *hostent;

    mUrl = url;

    std::string asStr = url.getHost();
    hostent = net::getHostByName(asStr.c_str());
    if (!hostent)
    {
        throw sys::SocketException(
            Ctxt(FmtX("net::getHostByName() failed for creation \"%s\"",
                      url.toString().c_str())) );
    }

    net::SocketAddress sa;
    sa.setPort(url.getPort());
    // Add this to class???
    ::memcpy(&(sa.getAddress().sin_addr.s_addr),
             hostent->h_addr,
             hostent->h_length);
    return create(sa);
}


net::NetConnection* net::NetConnectionClientFactory::newConnection(net::Socket toServer)
{
    return new net::NetConnection(toServer);
}


net::NetConnection * net::NetConnectionClientFactory::create(const net::SocketAddress& address)
{
    net::Socket socket = net::TCPClientSocketFactory().create(address);
    return newConnection(socket);
//     return new net::NetConnection(socket);

}