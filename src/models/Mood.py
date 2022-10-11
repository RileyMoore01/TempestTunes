from enum import Enum

class Mood(Enum):
    Happy = 1
    Sad = 2
    Tired = 3
    Cozy = 4
    Dancing = 5


for i in Mood:
    print(i)