#!/usr/bin/env python3

from message_class import message
from msg_generator import msg_generator
import re
import sys

def main():
    # import files:
    definitionsList = list()
    for filepath in sys.argv[1:]:
        # import file
        file = open(filepath, mode='r', encoding = 'latin-1').read()
        # remove header and footer from file, we do not need it.
        if ';' in file:
            header, definitions = file.split(';',1)
        elif 'BEGIN' in file:
            header, definitions = file.split('BEGIN',1)
        definitions = definitions.lstrip()
        # split the file into a list of strings, each containig the structure of what will 
        # later be one message.
        # get the ones with '{}'
        regex = re.compile('(.*)::=(.*){([\S\s]*?)}')
        List = regex.findall(definitions)
        definitionsList = definitionsList + List
        # get the oneliners without '{}'
        regex = re.compile('(\S*)\s*::=\s*([a-zA-Z][^{]*?)\n')
        definitionsList = definitionsList + regex.findall(definitions)
    # create a List of Messages
    messagesList = list()
    # create a List of message types and types used for variables in the Message for
    # analysing later.
    messagesTypesList = list()
    varTypesList = list()
    # create an object of each definition.
    for definition in definitionsList:
        messagesList.append(message(definition))
        # Print some helpful information, uncomment the second if-line for filtering.
        if True:
        #if messagesList[len(messagesList)-1].type == 'SEQUENCEOF':
            print(definition)
            print('- converts to -')
            print('name   : ' + str(messagesList[len(messagesList)-1].name))
            print('type   : ' + str(messagesList[len(messagesList)-1].type))
            print('content: ' + str(messagesList[len(messagesList)-1].content))
            try:
                print('sequeof: ' + str(messagesList[len(messagesList)-1].sequenceof))
            except:
                pass
            try:
                print('varlist: ' + str(messagesList[len(messagesList)-1].varlist))
            except:
                pass
            print('--')
        # Update the lists used for analysis.
        if messagesList[len(messagesList)-1].type not in messagesTypesList:
            messagesTypesList.append(messagesList[len(messagesList)-1].type)
        try:
            for e in messagesList[len(messagesList)-1].varlist.values():
                if e not in varTypesList:
                    varTypesList.append(e)
        except:
            # varlist might not exist depending on the message type.
            pass

    # print some Statistics:
    print('found Message versions:')
    print(messagesTypesList)
    print('found var types:')
    print(varTypesList)

    # compare the types defined with the types used.
    unknown_types = list()
    msggen = msg_generator()
    for varType in varTypesList:
        found = False
        for msg in messagesList:
            if varType == msg.name:
                found = True
                break
        if found:
            continue
        for type in msggen.knowntypes:
            if varType == type:
                found = True
                break
        if found:
            continue
        for type in msggen.convertibletypes:
            if varType == type[0]:
                found = True
                break
        if found:
            continue
        if not found:
            regex = re.compile('-?[0-9]+')
            if regex.match(varType) == None:
                unknown_types.append(varType)

    print('unknown types:')
    print(unknown_types)


if __name__ == '__main__':
    main()