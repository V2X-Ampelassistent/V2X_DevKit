import re

class message:
    def __init__(self, asn1definition):
        self.name = asn1definition[0].strip()
        # in some cases, there might be curly braces at name type side.
        if '{' in self.name:
            self.name, self.something = self.name.split('{', 1)
            self.name = self.name.strip()
        self.asn1def = asn1definition
        # disassemble the oneliners
        if len(asn1definition) == 2:
            # get type and content out of asn1definition
            defstr = asn1definition[1].strip()
            regex = re.compile('(BIT STRING|[a-zA-Z0-9]*)[\s]?(.*)?')
            regout = regex.findall(defstr)
            self.type = regout[0][0].strip()
            self.content = regout[0][1].strip()
            # individual handling for different types
            if self.type == 'SEQUENCE':
                # SEQUENCE in oneliners is always a SEQUENCEOF (a list)
                # the second part of the previous regout will always be the type of the sequence.
                regex = re.compile('(.*)OF(.*)')
                regout = regex.findall(regout[0][1])
                self.type = 'SEQUENCEOF'
                self.sequenceof = regout[0][1].strip()
        # disassemble multi-line structures
        elif len(asn1definition) == 3:
            # get type and content out of asn1definition
            self.type = asn1definition[1].strip()
            self.content = asn1definition[2].strip().split(',')
            # create varlist for later. it will contain the variable names and the type in a dictionary.
            self.varlist = dict()
            # individual handling for different types
            if (self.type == 'INTEGER') or (self.type == 'ENUMERATED') or (self.type == 'BIT STRING'):
                # INTEGER, ENUMERATED and BIT STRING share the same general structure, but might later
                # be handled individually.
                for e in self.content:
                    regex = re.compile('([0-9a-zA-Z]*) *\((.*?)\)' )
                    regout = regex.findall(e)
                    if regout:
                        self.varlist[regout[0][0]] = regout[0][1]
            elif (self.type == 'SEQUENCE') or (self.type == 'CHOICE'):
                # SEQUENCE and CHOICE share the same general structure, but might later be handled
                # individually.
                for e in self.content:
                    e = e.strip()
                    # remove part behind "("
                    e = e.split('(')
                    # split at space
                    var = e[0].split()
                    if (len(var) < 2) and ('...' not in var[0]):
                        raise Exception('var length too short.')
                    elif (len(var) >= 2):
                        var[1] = var[1].lstrip('[] 0-9')
                        self.varlist[var[0]] = var[1]
        else:
            raise Exception('Something is wrong' + str(asn1definition))
