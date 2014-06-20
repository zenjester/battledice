# battledice.py a simple test python game
# andyp 11.04.14

from dieRoller import *

def compCreate():
    return('creating computer team')

def playerCreate():
    return('create player team')

print('welcome to battledice')
print(compCreate())
print(playerCreate())
print('your roll is',dirRoll(4)) 
