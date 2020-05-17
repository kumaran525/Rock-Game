import random
a=['rock','paper','scissor']

p1=input("Player1 option:")
if p1 not in a:
    print('invalid sign')
else:
    p2=random.choice(a)
    print(p2)
    if (p1 == 'rock' and p2 == 'scissor'):
        print('Player1 wins')
    elif p1=='scissor' and p2=='rock':
        print('player2 wins')
    if p1=='rock' and p2=='paper':
        print('PLayer2 wins')
    elif p1=='paper' and p2=='rock':
        print('player1 wins')
    if (p1 == 'paper' and p2 == 'scissor'):
        print('PLayer2 wins')
    elif p1=='scissor' and p2=='paper':
        print('player1 wins')
    elif  p1==p2:
        print('Tie')

    
