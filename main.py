print('welcome to pokemon battle')
x = 10
print('vida = ', x)

# how we going to code the 'life system'

while x > 0:
  print('chegou a hora de escolher seu pokemon!')
  
  # here, will be the pokemon choice
  
  f = int(input('digite aqui seu numero de atks '))
  x = x - f
  if (x <= 0):
      print('game over')
  else:
      print('agora a vida é ', x)
