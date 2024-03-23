'''Rock, paper, scissors game
Create a program that allows the user to play
the classic game of rock, paper, scissors
against the computer. '''


import random
action = ["stone","paper","scissor"]


def round(action):
    
   
    position_1=player(action)
    print()
    print(f"you chose : {position_1}")

    position_2 = computer(action)
    print(f"computer chose : {position_2}")
    print()
    result = win_condtion(position_1,position_2)
    if(result == position_1):
        print("....you WIN....   :)")
        print()
    elif(result == position_2):
        print("....Computer WIN....")
        print()
    elif(result == False):
        print("...Match Tie...")
        print()

        

def player(action):

    print()
    print(f"1.{action[0]} | 2.{action[1]} | 3.{action[2]}")
    print()
    chi1 = (input("enter a your action(1/2/3) : "))
    while chi1 not in['1','2','3']:
        print("Invalid action--")
        chi1 = (input("enter a your action(1/2/3) : "))
    
    if(chi1 == '1'):
        return(action[0])
    elif(chi1=='2'):
        return(action[1])
    elif(chi1=='3'):
        return(action[2])

def computer(action):
    chi = random.choice(action)
    return(chi)

def win_condtion(position_1, position_2):

    if(position_1 == "stone" and position_2 == "scissor"):
        return position_1
    
    elif(position_1 == "scissor" and position_2 == "paper"):
        return position_1
    
    elif(position_1 == "paper" and position_2 == "stone"):
        return position_1
    
    elif(position_1 == "scissor" and position_2 == "stone"):
        return position_2
    
    elif(position_1 == "paper" and position_2 == "scissor"):
        return position_2
    
    elif(position_1 == "stone" and position_2 == "paper"):
  
        return position_2
    elif(position_1 == position_2):
        return False
    
counter = 0
while(True):
    
    if(counter == 0):
        round(action)
        counter += 1
    else:
        process = (input("you want to play again(yes/no) : "))
        if(process == 'yes'):
            round(action)
        if(process=="no"):
            break
        if process not in ['yes','no']:
            print('Invalid choice ')

print()
print("Thanku for playing game....")
print("Visit Again...")
