import os
from numpy import random

print("Welcome to pokemon battle")

# my  information
myLife = 100
print("Pokemon's = ", myLife, " HP \n")

# cleaning
clear = lambda: os.system('clear')

#oponent
oponent = "Team Rocket"
oponentLife = 100
dano = random.randint(5, 10)

# here, will be the pokemon choice

if(1):
  print("It's time to choose your pokemon!")
  print("Enter a number: \n 1 -> Pikachu \n 2 -> Squirtle \n 3 -> Bulbasaur")
  
  option = ""
  while option == "":
    option = input("Pokemon: ")
    
    if(option == "1"or option == "2" or option == "3"):
      
      if option == "1":
        pokemon = "Pikachu"
        
      if option == "2":
        pokemon = "Squirtle"
        
      if option == "3":
        pokemon = "Bulbasaur"
        
    else:
      print("não encontrei o pokemon selecionado \n por favor, tente novamente")
      exit()

clear()
print(pokemon, " eu escolho voce!")
while myLife > 0:

  myAtack = int(input("\n digite aqui seu numero de atks: "))
  
  myLife = myLife - dano
  oponentLife = oponentLife - myAtack
  clear()
  if (myLife <= 0):
      print("\n you lost, game over")
  elif oponentLife <= 0:
    print("\n you win!")
    exit()
  else:
      print("\n", oponent, " atacou você: -", dano, "  de HP \n")
      print( pokemon, ": ", myLife, " HP")
      print(oponent, ": ", oponentLife, " HP")
