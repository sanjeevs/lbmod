class LBError(Exception):
    pass

class DuplicateRecordError(LBError):
    pass

class NoRecordFoundError(LBError):
    pass