a = 0
b = 0
import random
random_options=('rock','paper','scissors')
player1=(input('enter your option'))


for i in range(5):
    if player1 == random_options:
        print("the game is a tie")
    elif player1 == 'rock'and random_options=='scissors':
        a +=1
        print('player1 is winner')
    elif player1 =='paper'and random_options=='rock':
        a +=1
        print('player1 is winner')
    elif player1 =='scissors' and random_options=='paper':
         a +=1
         print('player1 is winner')
    elif random_options=='scissors'and player1 =='paper' :
        b +=1
        print('computer is winner')  
    elif  random_options=='rock'and player1 =='scissors'  :
        b +=1
        print('computer is winner')
    else:
        b +=1
        print('computer is winner')
        print('the score of player1 is'+str(a))
        print('the score of computer is'+str(b))
    if a>b:
        print ('the winner is player1')
    elif b>a:
        print('the winner is computer')
    else:
        print('the game is draw')