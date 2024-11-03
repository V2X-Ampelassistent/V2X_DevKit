import re

class message:
    def __init__(self, asn1definition):
        self.name = asn1definition[0].strip()
        self.asn1def = asn1definition
        if len(asn1definition) == 2:
            defstr = asn1definition[1].strip()
            regex = re.compile('(BIT STRING|[a-zA-Z0-9]*)[\s]?(.*)?')
            regout = regex.findall(defstr)
            self.type = regout[0][0].strip()
            self.content = regout[0][1].strip()
            if self.type == 'SEQUENCE':
                regex = re.compile('(.*)OF(.*)')
                regout = regex.findall(regout[0][1])
                print(regout)
                self.type = 'SEQUENCEOF'
                self.sequenceof = regout[0][1].strip()
        elif len(asn1definition) == 3:
            # make a 2D list for each variable Pair
            self.type = asn1definition[1].strip()
            self.content = asn1definition[2].strip().split(',')
            self.varlist = dict()
            if (self.type == 'INTEGER') or (self.type == 'ENUMERATED') or (self.type == 'BIT STRING'):
                for e in self.content:
                    regex = re.compile('([0-9a-zA-Z]*) *\((.*?)\)' )
                    regout = regex.findall(e)
                    if regout:
                        self.varlist[regout[0][0]] = regout[0][1]
            elif (self.type == 'SEQUENCE') or (self.type == 'CHOICE'):
                for e in self.content:
                    e = e.strip()
                    var = e.split()
                    if (len(var) < 2) and ('...' not in var[0]):
                        raise Exception('var length too short.')
                    elif (len(var) >= 2):
                        self.varlist[var[0]] = var[1]
        else:
            raise Exception('Something is wrong' + str(asn1definition))
