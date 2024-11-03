
class msg_generator:

    convertibletypes = list((('IA5String', 'string'), ('UTF8String', 'string')))
    
    knowntypes = list(('SEQUENCE', 'SEQUENCEOF', 'CHOICE', 'INTEGER', 'BOOLEAN'))

    def __init__(self):
        pass