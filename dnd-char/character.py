# A class for maintaining character information

from enum import Enum

class Attributes(Enum):
    STR = 0
    DEX = 1
    CON = 2
    INT = 3
    WIS = 4
    CHA = 5

class Character():
    def __init__(self):
        self.attributes = [[10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 0]]
        return
    
    def getAttributeValue(self, attr):
        return self.attributes[attr][0]

    def setAttributeValue(self, attr, val)
        self.attributes[attr][0] = val
        return

    def getAttributeMod(self, attr):
        return