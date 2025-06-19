import os
from gameLogic import Game
from gameLogic import HowToPlay

#Running python in terminal: python main.py
def main():
  canPlay = True

  while(canPlay):
    os.system("clear")
    print("======================================")
    print("    WELCOME TO ROCK PAPER SCISSORS    ")
    print("======================================\n\n")
    print("1. Play Game")
    print("2. How To Play")
    print("3. Exit Game\n\n")
    
    option = int(input("Select an option: "))
    if(option == 1):
      Game()
    elif(option == 2):
      HowToPlay()
    elif(option == 3):
      break

if __name__ == "__main__":
  main()