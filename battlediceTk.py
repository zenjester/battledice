# battledice.py a simple test python game
# andyp 11.04.14
# Tkinter Version

import dieRoller
import tkinter


def compCreate():
    return 'creating computerteam'


def playerCreate():
    return 'create player team'

"""main function """
turn = 0  # turn variable
playerTxt = playerCreate()
aiTxt = compCreate()
msgTxt = 'Welcome to the game'
rollTxt = 'the roll is ' + dieRoller.dirRoll(6)
app = tkinter.Tk()
# set up widgets area
playerArea = tkinter.Text(app, height=23, width=50, bg='green', fg='white')
aiArea = tkinter.Text(app, height=23, width=50, bg='red')
msgArea = tkinter.Text(app, height=20, width=50, bg='cyan')
rollArea = tkinter.Text(app, height=10, width=50, bg='yellow')
playerArea.insert(1.0, 'Player Team\n')
playerArea.insert(2.0, playerTxt)
aiArea.insert(2.9, aiTxt)
msgArea.insert('1.0', msgTxt)
msgArea.insert('2.0', msgTxt)
rollArea.insert(0.0, rollTxt)
turnBtn = tkinter.Button(app, text='Next Turn', width=10)
saveBtn = tkinter.Button(app, text='save', width=10)
quitBtn = tkinter.Button(app, text='quit', width=10)
app.title('BattleDice')
#grid it
playerArea.grid(row=0, column=0, columnspan=2)
aiArea.grid(row=0, column=2)
msgArea.grid(row=1, column=0, columnspan=2)
rollArea.grid(row=1, column=2)
quitBtn.grid(row=2, column=0)
saveBtn.grid(row=2, column=1)
turnBtn.grid(row=2, column=2)
app.mainloop()

