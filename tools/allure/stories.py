from enum import Enum

class AllureStory(str, Enum):
    COURSES = 'courses'
    DASHBOARD = 'dashboard'
    REGISTRATION = 'registration'
    AUTHORISATION = 'authorisation'