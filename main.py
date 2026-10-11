# STONE PAPER SCICOR
Apoint = int(0)
import random
Bpoint = int(0)
turns = int(3)
while turns > 0:
    i=1
    try:
         p1 = input(str("P1. Stone , paper , scicor : ")).lower()
    except ValueError:
        print("Enter from the above choices") 
    
    c = ['stone' ,' paper' ,'scicor']
    p2 = random.choice(c)

    if p1==p2:
        print("Its a tie !")
        print(f'Current score is {Apoint} - {Bpoint }')
    elif (p1=='stone' and p2=='scicor') or  ( p1=='paper' and p2 == 'stone') or ( p1=='scicor' and p2=='paper') :
        print(f" Player 1 is winner of turn {i} ")
        Apoint = Apoint + 1
        print(f"Computer selected {p2} ")
        print(f'Current score is {Apoint} - {Bpoint }')
    else:
        print(f" Player 2 is winner of turn {i} ")
        print(f"Computer selected {p2} ")
        Bpoint = Bpoint + 1  
        print(f'Current score is {Apoint} - {Bpoint }')
    if Apoint > Bpoint:
        print('Player 1 is winner')
    else:
        print('Player 2 is winner')   
    i=+1
    turns = turns-1
        
