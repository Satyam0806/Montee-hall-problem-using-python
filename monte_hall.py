#monte hall problem
import random
doors=[0]*3
goatdoor=[0]*2
swap=0 #number of swap wins
dont_swap=0 #number of dont swp wins
j=0
while(j<5): #here we have given the user 5 chances to identify his winnings and loss 
    x=random.randint(0,2) # xwill comprise of bmw door
    doors[x]='BMW'
    for i in range(0,3):
        if(i==x):
            continue
        else:
            doors[i]='Goat'
            goatdoor.append(i)
    choice=int(input('enter your choice from 0,1,2 : '))
    door_open=random.choice(goatdoor)  # we can only open the door that contains the goat
    while(door_open==choice):  #door open shouldnt be equalt to choice made by teh user
        door_open=random.choice(goatdoor)
    ch=input('Do you want to swap? y/n : ')
    if(ch=="y"):
        if(doors[choice]=='Goat'):
            print('Winner')
            swap=swap+1
        else:
            print('lost')
    else:
        if(doors[choice]=='Goat'):
            print("player lost")
        else:
            print("You Won")
            dont_swap=dont_swap+1 
    j=j+1

print(f'the winns you get when you swap are {swap}')
print(f'the winns you get when you dont_swap are {dont_swap}')