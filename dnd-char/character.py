# A class for maintaining character information

# TODO: Add comments
# TODO: Read over other attributes to add them to here

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
        # first value is attr score, second is percentile if 18
        self.attributes = [[10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 0]]
        return
    
    def getAttributeValue(self, attr):
        return self.attributes[attr][0]

    def setAttributeValue(self, attr, val):
        self.attributes[attr][0] = val
        return

    def getStrHitMod(self):
        if self.attributes[0][0] == 3:
            return -3
        elif self.attributes[0][0] == 4 or self.attributes[0][0] == 5:
            return -2
        elif self.attributes[0][0] == 6 or self.attributes[0][0] == 7:
            return -1
        elif self.attributes[0][0] >= 8 and self.attributes[0][0] <= 16:
            return 0
        elif self.attributes[0][0] == 17:
            return 1
        elif self.attributes[0][0] == 18:
            if self.attributes[0][1] >= 0 and self.attributes[0][1] <= 50:
                return 1
            elif self.attributes[0][1] >= 51 and self.attributes[0][1] <= 99:
                return 2
            elif self.attributes[0][1] == 100:
                return 3
        raise ValueError("STR attribute not between 3-18/00")

    def getStrDmgMod(self):
        if self.attributes[0][0] >= 3 and self.attributes[0][0] <= 5:
            return -1
        elif self.attributes[0][0] >= 6 and self.attributes[0][0] <= 15:
            return 0
        elif self.attributes[0][0] == 16 or self.attributes[0][0] == 17:
            return 1
        elif self.attributes[0][0] == 18:
            if self.attributes[0][1] == 0:
                return 2
            elif self.attributes[0][1] >= 1 and self.attributes[0][1] <= 75:
                return 3
            elif self.attributes[0][1] >= 76 and self.attributes[0][1] <= 90:
                return 4
            elif self.attributes[0][1] >= 91 and self.attributes[0][1] <= 99:
                return 5
            elif self.attributes[0][1] == 100:
                return 6
        raise ValueError("STR attribute not between 3-18/00")

    def getDexHitMod(self):
        if self.attributes[1][0] == 3:
            return -3
        elif self.attributes[1][0] == 4:
            return -2
        elif self.attributes[1][0] == 5:
            return -1
        elif self.attributes[1][0] >= 6 and self.attributes[1][0] <= 15:
            return 0
        elif self.attributes[1][0] == 16:
            return 1
        elif self.attributes[1][0] == 17:
            return 2
        elif self.attributes[1][0] == 18:
            return 3
        raise ValueError("DEX attribute not between 3-18")
    
    def getDexDefMod(self):
        if self.attributes[1][0] == 3:
            return 4
        elif self.attributes[1][0] == 4:
            return 3
        elif self.attributes[1][0] == 5:
            return 2
        elif self.attributes[1][0] == 6:
            return 1
        elif self.attributes[1][0] >= 7 and self.attributes[1][0] <= 14:
            return 0
        elif self.attributes[1][0] == 15:
            return -1
        elif self.attributes[1][0] == 16:
            return -2
        elif self.attributes[1][0] == 17:
            return -3
        elif self.attributes[1][0] == 18:
            return -4
        