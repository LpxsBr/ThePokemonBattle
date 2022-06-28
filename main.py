print('welcome to pokemon battle')
x = 10
print('vida = ', x)

# how we going to code the 'life system'

while x > 0:
  f = int(input('digite aqui seu numero de atks '))
  x = x - f
  if(x == 0):
    print('voce morreu, vida =', x)
  else:
    print('agora a vida é ',x)