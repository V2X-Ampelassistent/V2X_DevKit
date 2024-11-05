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
        elif len(asn1definition) >= 3:
            # get type and content out of asn1definition
            self.type = asn1definition[1].strip()
            # split content at every comma that is not inside of brackets:
            self.content = re.split(',\s*(?![^()]*\))', asn1definition[2])

            # create varlist for later. it will contain the variable names and the type in a dictionary.
            self.varlist = dict()

            # Output of regex will be:
            _pos_variable = 0
            _pos_of = 1
            _pos_number = 2
            _pos_implicit_explicit = 3
            _pos_type = 4
            _pos_trailer = 5

            regex = re.compile('([-a-zA-Z0-9]+)\s+(OF\s)?\s*(\[[0-9]*\]\s+)?(EXPLICIT\s+|IMPLICIT\s+)?([-a-zA-Z0-9]+)?([\S\s]*)')
            self.contents_list = list()
            for e in self.content:
                regout = regex.findall(e)
                self.contents_list.append(regout)
                if regout:
                    self.varlist[regout[0][_pos_variable]] = regout[0][_pos_type]
