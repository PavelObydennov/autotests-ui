from enum import Enum

class AllureEpic(str, Enum):
    LMS = "LMS system"
    STUDENT = 'STUDENT system'
    ADMINISTRATION = 'ADMINISTRATION system'