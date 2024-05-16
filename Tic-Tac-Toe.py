# Created by Erick Delgado

import random
import turtle

#Initial variables
msg1 = "Player 1 "
msg2 = "Player 2 "
msg3 = "Computer "

numMoves = 0

gamerunning = True

global playerOneTurn
playerOneTurn = True

playerOneChoice = []
playerTwoChoice = []

#Screen
screen = turtle.Screen()
screen.title('TIC TAC TOE')
screen.bgcolor('teal')

#Positional turtles
pos_1 = turtle.Turtle()
pos_1.ht()
pos_1.speed('fastest')
pos_1.penup()
pos_1.goto(-80,80)

pos_2 = turtle.Turtle()
pos_2.speed('fastest')
pos_2.ht()
pos_2.penup()
pos_2.goto(0,80)

pos_3 = turtle.Turtle()
pos_3.speed('fastest')
pos_3.ht()
pos_3.penup()
pos_3.goto(80,80)

pos_4 = turtle.Turtle()
pos_4.speed('fastest')
pos_4.ht()
pos_4.penup()
pos_4.goto(-80,0)

pos_5 = turtle.Turtle()
pos_5.speed('fastest')
pos_5.ht()
pos_5.penup()
pos_5.goto(0,0)

pos_6 = turtle.Turtle()
pos_6.speed('fastest')
pos_6.ht()
pos_6.penup()
pos_6.goto(80,0)

pos_7 = turtle.Turtle()
pos_7.speed('fastest')
pos_7.ht()
pos_7.penup()
pos_7.goto(-80,-80)

pos_8 = turtle.Turtle()
pos_8.speed('fastest')
pos_8.ht()
pos_8.penup()
pos_8.goto(0,-80)

pos_9 = turtle.Turtle()
pos_8.speed('fastest')
pos_9.ht()
pos_9.penup()
pos_9.goto(80,-80)

movesList = [pos_1, pos_2, pos_3, pos_4, pos_5, pos_6, pos_7, pos_8, pos_9]

#Numbers in Grid
style3 = ('Courier', 15, 'italic')
Num_1 = turtle.Turtle()
Num_1.ht()
Num_1.speed('fastest')
Num_1.penup()
Num_1.goto(-55,40)
Num_1.color('lightgreen')
Num_1.write('1',font= style3)

Num_2 = turtle.Turtle()
Num_2.ht()
Num_2.speed('fastest')
Num_2.penup()
Num_2.goto(25,40)
Num_2.color('lightgreen')
Num_2.write('2',font= style3)

Num_3 = turtle.Turtle()
Num_3.ht()
Num_3.speed('fastest')
Num_3.penup()
Num_3.goto(105,40)
Num_3.color('lightgreen')
Num_3.write('3',font= style3)

Num_4 = turtle.Turtle()
Num_4.ht()
Num_4.speed('fastest')
Num_4.penup()
Num_4.goto(-55,-40)
Num_4.color('lightgreen')
Num_4.write('4',font= style3)

Num_5 = turtle.Turtle()
Num_5.ht()
Num_5.speed('fastest')
Num_5.penup()
Num_5.goto(25,-40)
Num_5.color('lightgreen')
Num_5.write('5',font= style3)

Num_6 = turtle.Turtle()
Num_6.ht()
Num_6.speed('fastest')
Num_6.penup()
Num_6.goto(105,-40)
Num_6.color('lightgreen')
Num_6.write('6',font= style3)

Num_7 = turtle.Turtle()
Num_7.ht()
Num_7.speed('fastest')
Num_7.penup()
Num_7.goto(-55,-120)
Num_7.color('lightgreen')
Num_7.write('7',font= style3)

Num_8 = turtle.Turtle()
Num_8.ht()
Num_8.speed('fastest')
Num_8.penup()
Num_8.goto(25,-120)
Num_8.color('lightgreen')
Num_8.write('8',font= style3)

Num_9 = turtle.Turtle()
Num_9.ht()
Num_9.speed('fastest')
Num_9.penup()
Num_9.goto(105,-120)
Num_9.color('lightgreen')
Num_9.write('9',font= style3)

#Grid code
def Grid():
  grid = turtle.Turtle()
  grid.ht()
  grid.speed('fastest')
  grid.pensize(4)
  grid.penup()
  grid.goto(40,-120)
  grid.pendown()
  grid.goto(40,120)
  grid.penup()
  grid.goto(-40,120)
  grid.pendown()
  grid.goto(-40,-120)
  grid.penup()
  grid.goto(-120,-40)
  grid.pendown()
  grid.goto(120,-40)
  grid.penup()
  grid.goto(-120,40)
  grid.pendown()
  grid.goto(120,40)
  grid.penup()
  grid.goto(0,160)
  grid.color('white')
  style1 = ('Courier', 30, 'italic')
  grid.write('TIC -TAC- TOE ',font= style1, align='center')


#Drawing Functions
def DrawX(pos):
  pos.color('DarkBlue')
  pos.pensize(5)
  pos.penup()
  pos.setheading(45)
  pos.pendown()
  pos.fd(40)
  pos.bk(80)
  pos.fd(40)
  pos.setheading(135)
  pos.fd(40)
  pos.bk(80)
  pos.fd(40)

def DrawO(pos):
  pos.color('DarkRed')
  pos.pensize(5)
  pos.penup()
  pos.setheading(90)
  pos.bk(32)
  pos.pendown()
  pos.setheading(0)
  pos.circle(32)
  pos.penup()
  pos.setheading(90)
  pos.fd(32)


#Toss Coin to determine the first player to play
def tossCoin():
    choice = input ('pick heads or tails : ')
    while choice.lower() != 'heads' and choice.lower() != 'tails' :
        choice = input('You did not pick heads or tails, choose again : ')
  
    Coin = [ "tails", "heads" ]
    sideOfCoin = random.choice(Coin)

    playerOneTurn = False

    message = "PlayerTwo STARTS !"
    if choice.lower() == sideOfCoin :
        playerOneTurn = True
        message = 'PlayerOne STARTS !'
    print ('The coin side is :', sideOfCoin)
    print (message)
    
    return playerOneTurn

#appends the player's choice on his list and uses one of the 2 drawing functions        
def playerchoice(alist1, alist2, msg, Draw):
    print(msg)
    choice = str(input('Chose a placement : '))

    while not(choice.isdigit()):
        print(msg)
        choice = str(input('ERROR / Choose valid placement : '))

    while (int(choice) < 1 or int(choice) > 9) or (choice in alist1 or choice in alist2):
        print(msg)
        choice = str(input('ERROR / Choose valid placement : '))
      
    for i in range(0, 9):
        if int(choice) == i + 1 :
            alist1.append(choice)
            Draw(movesList[i])
      
#appends the player's / computer choice on the lists and uses one of the 2 drawing functions  
def playerCompchoice(alist1, alist2, msg, Draw, numMoves, isHuman):
  if isHuman is True:
    print(msg)
    choice = str(input('Chose a placement : '))

    while not(choice.isdigit()):
      choice = str(input('ERROR / Choose valid placement : '))

    while (int(choice) < 1 or int(choice) > 9) or (choice in alist1 or choice in alist2):
        choice = str(input('ERROR / Choose valid placement : '))
      
  else:
    choice = str(random.randint(1,9))
    print(msg)
    while (choice in alist1 or choice in alist2): 
      choice = str(random.randint(1,9))
        
        
  for i in range(0, 9):
    if int(choice) == i + 1 :
      alist1.append(choice)
      Draw(movesList[i])   
    
victory= turtle.Turtle()
victory.ht()
victory.speed('fastest')
victory.penup()
victory.goto(0,-180)
victory.color('SkyBlue')
style = ('Courier', 25, 'italic')

#Checks if the items in the list or the number of moves stops the game
#or if the game should pursue if it is neither a tie nor someone won
def checkWin(alist, numMoves):
  
  for i in range(1,8,3):
      if str(i) in alist and str(i + 1) in alist and str(i + 2) in alist:
          print('YOU WON')
          movesList[i - 1].setheading(0)
          movesList[i - 1].color("white")
          movesList[i - 1].pendown()
          movesList[i - 1].fd(160)
          victory.write('YOU WON !!! ',font= style, align='center')
          return False
          

  for i in range(1,4):
      if str(i) in alist and str(i + 3) in alist and str(i + 6) in alist:
          print('YOU WON')
          movesList[i - 1].setheading(270)
          movesList[i - 1].color("white")
          movesList[i - 1].pendown()
          movesList[i - 1].fd(160)
          victory.write('YOU WON !!! ',font= style, align='center')
          return False
            

  if "3" in alist and "5" in alist and "7" in alist:
      print('YOU WON')
      pos_3.color('white')
      pos_3.pendown()
      pos_3.goto(-80,-80)
      victory.write('YOU WON !!! ',font= style, align='center')
      return False

  if "1" in alist and "5" in alist and "9" in alist:
      print('YOU WON')
      pos_1.color('white')
      pos_1.pendown()
      pos_1.goto(80,-80)
      victory.write('YOU WON !!! ',font= style, align='center')
      return False
    
  if numMoves == 8:
    print("It's a TIE")
    victory.write('TIE !!! ',font= style, align='center')
    return False
  
  return True

Grid()  
#Game loop
gameMode = input('Choose game mode solo or multiplayer : ')
while gameMode.lower() != 'solo' and gameMode.lower() != 'multiplayer' :
      gameMode = input('You did not pick solo or multiplayer, choose again : ')

if gameMode.lower() == 'solo':
  playerOneTurn = tossCoin()
  while gamerunning == True:
    if playerOneTurn == True:
      playerCompchoice(playerOneChoice, playerTwoChoice, msg1, DrawX, numMoves, True)
      gamerunning = checkWin(playerOneChoice, numMoves)
      playerOneTurn = False
      numMoves += 1
      
    else:
      playerCompchoice(playerTwoChoice, playerOneChoice, msg2, DrawO, numMoves, False)
      gamerunning = checkWin(playerTwoChoice, numMoves)
      playerOneTurn = True
      numMoves += 1

else:
  playerOneTurn = tossCoin()
  while gamerunning == True:
    if playerOneTurn == True:
      playerchoice(playerOneChoice, playerTwoChoice, msg1, DrawX)
      gamerunning = checkWin(playerOneChoice, numMoves)
      playerOneTurn = False
      numMoves += 1         
    else:
      playerchoice(playerTwoChoice, playerOneChoice, msg2, DrawO)
      gamerunning = checkWin(playerTwoChoice,numMoves)
      playerOneTurn = True
      numMoves += 1

input('Press ENTER to exit')
