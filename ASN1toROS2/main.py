#!/usr/bin/env python3

from message_class import message
import re
import sys

def main():
    file = open(sys.argv[1], mode='r', encoding = 'latin-1').read()
    if ';' in file:
        header, definitions = file.split(';',1)
    elif 'BEGIN' in file:
        header, definitions = file.split('BEGIN',1)
    definitions = definitions.lstrip()
    definitions = definitions.rstrip('END \n')
    # get the ones with '{}'
    regex = re.compile('(.*) ::= (.*){([\S\s]*?)}')
    definitionsList = regex.findall(definitions)
    #definitionsList = list()
    # get the oneliners without '{}'
    regex = re.compile('(\S*)\s*::=\s*([a-zA-Z][^{]*?)\n')
    definitionsList = definitionsList + regex.findall(definitions)
    # create a List of Messages
    messagesList = list()
    messagesTypesList = list()
    varTypesList = list()
    for definition in definitionsList:
        messagesList.append(message(definition))
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
        if messagesList[len(messagesList)-1].type not in messagesTypesList:
            messagesTypesList.append(messagesList[len(messagesList)-1].type)
        try:
            for e in messagesList[len(messagesList)-1].varlist.values():
                if e not in varTypesList:
                    varTypesList.append(e)
        except:
            pass


    print('found Message types:')
    print(messagesTypesList)
    print('found var types:')
    print(varTypesList)

    unknown_types = list()
    for varType in varTypesList:
        found = False
        for msg in messagesList:
            if varType == msg.name:
                found = True
        if not found:
            unknown_types.append(varType)

    print('unknown types:')
    print(unknown_types)


if __name__ == '__main__':
    main()