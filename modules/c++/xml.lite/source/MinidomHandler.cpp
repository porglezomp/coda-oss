/* =========================================================================
 * This file is part of xml.lite-c++ 
 * =========================================================================
 * 
 * (C) Copyright 2004 - 2009, General Dynamics - Advanced Information Systems
 *
 * xml.lite-c++ is free software; you can redistribute it and/or modify
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

#include "xml/lite/MinidomHandler.h"


void xml::lite::MinidomHandler::setNewDocument(Document *newDocument)
{
    if (mDocument != NULL)
    {
        if (newDocument == mDocument)
            return;
        delete mDocument;
    }
    mDocument = newDocument;
}

void xml::lite::MinidomHandler::clear()
{
    mDocument->destroy();
    currentCharacterData = "";
    assert(bytesForElement.empty());
    assert(nodeStack.empty());
}

/*==================================================*/
/* This marks the start of tree handler code        */
/*==================================================*/

void xml::lite::MinidomHandler::characters(const char *value, int length)
{
    // Append new data

    if (length)
        currentCharacterData += std::string(value, length);

    //    dbg_printf("Current Char Data: @@@%s@@@\n", currentCharacterData.c_str());
    // Append number of bytes added to this node's stack value
    assert(bytesForElement.size());
    bytesForElement.top() += length;
}

void
xml::lite::MinidomHandler::startElement(const std::string & uri,
                                        const std::string & localName,
                                        const std::string & qname,
                                        const xml::lite::Attributes & atts)
{
    // Assign what we can now, and push rest on stack
    // for later

//     dbg_printf("Local name: <%s>", localName.c_str() );
//     dbg_printf("Uri:        <%s>", uri.c_str() );
//     dbg_printf("QName:      <%s>", qname.c_str() );


    xml::lite::Element * current = mDocument->createElement(qname, uri);


    current->setAttributes(atts);
    // Push this onto the node stack
    nodeStack.push(current);
    // Push a size of zero bytes on stack for this node's
    // char data
    bytesForElement.push(0);
    //    dbg_printf("========================PUSH: <%d>=========================\n",
    //bytesForElement.size());

}

// This function subtracts off the char place from the push
std::string xml::lite::MinidomHandler::adjustCharacterData()
{
    // Edit the string with regard to this node's char data
    // Get rid of what we take on char data accumulator


    int diff =
        (int)(currentCharacterData.length()) -
        bytesForElement.top();

//     dbg_printf("Diff: %d", diff);
//     dbg_printf("Current Char Data Length: %d",
//             currentCharacterData.length());
    std::string newCharacterData(currentCharacterData.
                                 substr(diff, currentCharacterData.length()));
    assert(diff >= 0);
    currentCharacterData.erase(diff, currentCharacterData.length());
    if (!mPreserveCharData)
        trim(newCharacterData);

    return newCharacterData;
}

void
xml::lite::MinidomHandler::trim(std::string & s)
{
    int i;


    for (i = 0; i < (int)s.length(); i++)
    {
        if (!isspace(s[i]))
            break;
    }
    s.erase(0, i);


    for (i = (int)s.length() - 1; i >= 0; i--)
    {
        if (!isspace(s[i]))
            break;

    }
    if (i + 1 < (int)s.length())
        s.erase(i + 1);
}

void
xml::lite::MinidomHandler::endElement(const std::string & uri,
                                      const std::string & localName,
                                      const std::string & qname)
{
    // Pop current off top
    xml::lite::Element * current = nodeStack.top();
    nodeStack.pop();

    // Set final info for current

    //    EVAL(current->characterData.getDataSize());


    current->setCharacterData(adjustCharacterData());

//     dbg_printf("Finalized Character Data: [>>%s<<]",
//                   current->getCharacterData().c_str());

    // Remove corresponding int on bytes stack
    bytesForElement.pop();
    //    dbg_printf("========================POP: <%d>==========================\n",
    //bytesForElement.size());
    // Something is left on the stack
    // (We dont have not top-level node)
    if (nodeStack.size())
    {
        // Add current to child of parent
        //          std::cout << "Adding node: " << current.name << std::endl;
        //HERE();
        xml::lite::Element * parent = nodeStack.top();
        parent->addChild(current);
    }
    // This is the top-level node, and we are done
    // Just Assign
    else
    {
        //          OutputFileStream debug("Debug.xml");
        //          current.print(debug);
        //          debug.close();
        mDocument->setRootElement(current);
    }

}

void xml::lite::MinidomHandler::preserveCharacterData(bool preserve)
{
    mPreserveCharData = preserve;
}
