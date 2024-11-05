
class msg_generator:

    convertibletypes = {"IA5String": 'string', "UTF8String": 'string', 'INTEGER': 'int64', 'BOOLEAN' : 'uint8' }
    
    knowntypes = list(('SEQUENCE', 'SEQUENCEOF', 'CHOICE', 'NULL', 'ABSENT'))

    def __init__(self):
        pass