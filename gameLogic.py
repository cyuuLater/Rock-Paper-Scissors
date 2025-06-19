import random
import os
import time

# Important game logic variables
playerPoints = 0
aiPoints = 0
canPlay = True

# ANSI Variables
red = '\033[91m'
green = '\033[92m'
yellow = '\033[93m'
bold = '\033[1m'
reset = '\033[0m'

# Summary of score so far (player win)
def currentSummaryPlayer(aiBot, playAction):
  print("---------------------------------")
  print("           Player Point          ")
  print("---------------------------------\n")
  print("Player: " + bold + green + playAction.upper() + reset)
  print("AI Player: " + bold + red + aiBot + reset + "\n")
  print(f"Current Score: {playerPoints} - {aiPoints}\n\n")
  print("Waiting for next round...")
  time.sleep(5)

  os.system("clear")
  print("Rock, Paper, Scissors...")
  time.sleep(2)

# Summary of score so far (AI win)
def currentSummaryAI(aiBot, playAction):
  print("---------------------------------")
  print("         AI Player Point         ")
  print("---------------------------------\n")
  print("Player: " + bold + red + playAction.upper() + reset)
  print("AI Player: " + bold + green + aiBot + reset + "\n")
  print(f"Current Score: {playerPoints} - {aiPoints}\n\n")
  print("Waiting for next round...")
  time.sleep(5)

  os.system("clear")
  print("Rock, Paper, Scissors...")
  time.sleep(2)

# For winning attempts
def victory(aiBot, playAction):
  global canPlay
  global playerPoints
  global aiPoints
  
  while(canPlay):
    canPlay = False
    print("---------------------------------")
    print("           Player Wins!          ")
    print("---------------------------------\n")
    print("Player: " + bold + green + playAction.upper() + reset)
    print("AI Player: " + bold + red + aiBot + reset + "\n")
    print(f"Final Score: {playerPoints} - {aiPoints}")
    print("Congratulations!\n\n")
    
    playerPoints = 0
    aiPoints = 0
    
    enter = input("Press [enter] to exit")
    if(enter == ""):
      break

# For losing attempts
def loss(aiBot, playAction):
  global canPlay
  global playerPoints
  global aiPoints
  
  while(canPlay):
    canPlay = False
    print("---------------------------------")
    print("          AI Player Wins         ")
    print("---------------------------------\n")
    print("Player: " + bold + red + playAction.upper() + reset)
    print("AI Player: " + bold + green + aiBot + reset + "\n")
    print(f"Final Score: {playerPoints} - {aiPoints}") 
    print("Better luck next time!\n\n")
    
    playerPoints = 0
    aiPoints = 0
    
    enter = input("Press [enter] to exit")
    if(enter == ""):
      break

# For ties
def tie(aiBot, playAction):
  print("AI Player: " + bold + yellow + aiBot + reset)
  print("Player: " + bold + yellow + playAction.upper() + reset)
  print()
  print("Rock, Paper, Scissors...")
  time.sleep(2)

# Complete game logic
def Game():
  os.system("clear")
  global playerPoints
  global aiPoints
  global canPlay 

  # Important game logic variables
  playerPoints = 0
  aiPoints = 0
  canPlay = True

  aiBot = random.choice(["R", "P", "S"])
  print("Rock, Paper, Scissors...")
  time.sleep(2)
  playAction = input("Shoot: ")
  canPlay = True

  while(canPlay):
    ######  When the player picks scissors  ######
    if(playAction == "S" or playAction == "s"):
      os.system("clear")

      # Losing condition
      if(aiBot == "R"):      
        if(aiPoints == 1):
          aiPoints += 1
          loss(aiBot, playAction)
        else:
          aiPoints += 1
          currentSummaryAI(aiBot, playAction)
          aiBot = random.choice(["R", "P", "S"])
          playAction = input("Shoot: ")

      # Winning condition
      elif(aiBot == "P"):
        if(playerPoints == 1):
          playerPoints += 1
          victory(aiBot, playAction)
        else:
          playerPoints += 1
          currentSummaryPlayer(aiBot, playAction)
          aiBot = random.choice(["R", "P", "S"])
          playAction = input("Shoot: ")

      # A tie
      elif(aiBot == "S"):
        tie(aiBot, playAction)
        aiBot = random.choice(["R", "P", "S"])
        playAction = input("Shoot: ")


    ######  When the player picks paper  ######
    elif(playAction == "P" or playAction == "p"):
      os.system("clear")

      # Winning condition
      if(aiBot == "R"):
        if(playerPoints == 1):
          playerPoints += 1
          victory(aiBot, playAction)
        else:
          playerPoints += 1
          currentSummaryPlayer(aiBot, playAction)
          aiBot = random.choice(["R", "P", "S"])
          playAction = input("Shoot: ")

      # Losing attempt
      elif(aiBot == "S"):
        if(aiPoints == 1):
          aiPoints += 1
          loss(aiBot, playAction)
        else:
          aiPoints += 1
          currentSummaryAI(aiBot, playAction)
          aiBot = random.choice(["R", "P", "S"])
          playAction = input("Shoot: ")

      # Tie
      elif(aiBot == "P"):
        tie(aiBot, playAction)
        aiBot = random.choice(["R", "P", "S"])
        playAction = input("Shoot: ")
    

    ######  When the player picks rock  ######
    elif(playAction == "R" or playAction == "r"):
      os.system("clear")

      # Winning condition
      if(aiBot == "S"):
        if(playerPoints == 1):
          playerPoints += 1
          victory(aiBot, playAction)
        else:
          playerPoints += 1
          currentSummaryPlayer(aiBot, playAction)
          aiBot = random.choice(["R", "P", "S"])
          playAction = input("Shoot: ")

      # Losing condition
      elif(aiBot == "P"):
        if(aiPoints == 1):
          aiPoints += 1
          loss(aiBot, playAction)
        else:
          aiPoints += 1
          currentSummaryAI(aiBot, playAction)
          aiBot = random.choice(["R", "P", "S"])
          playAction = input("Shoot: ")

      # Tie
      elif(aiBot == "R"):
        tie(aiBot, playAction)
        aiBot = random.choice(["R", "P", "S"])
        playAction = input("Shoot: ")


    # What are you doing?
    else:
      os.system("clear")
      aiBot = random.choice(["R", "P", "S"])
      print("Rock, Paper, Scissors...")
      playAction = input("Shoot: ")

# How to play menu
def HowToPlay():
  os.system("clear")
  
  while(True):
    print("===========================================")
    print("                HOW TO PLAY                ")
    print("===========================================\n")

    print("Rock Paper Scissors is a decision making")
    print("game, and you'll be playing against an AI") 
    print("player.\n\n")

    print("When it says shoot, pick a corresponding")
    print("letter to the choice you'll make:")

    print("- " + bold + "R " + reset + "stands for Rock")
    print("- " + bold + "P " + reset + "stands for Paper")
    print("- " + bold + "S " + reset + "stands for Scissors\n")

    print("The winning conditions are as follows:")

    print("- Rock beats Scissors")
    print("- Paper beats Rock")
    print("- Scissors beats Paper\n\n")

    print("A victory will be based on whoever wins at")
    print("least 2 of 3 rounds.\n\n")
    
    enter = input("Press [enter] to exit")
    if(enter == ""):
      break