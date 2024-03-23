''' Tic Tac Toe Game
Create a simple Tic Tac Toe game that can be'
played between two players '''

def condition(board, SYM):
    if board[0][0] == board[0][1] == board[0][2] == SYM:
        print("\n")
        print(f"PLAYER {SYM} WILL BE WIN ......!!!!")
        print("\n")
        return True
    
    elif board[1][0] == board[1][1] == board[1][2] == SYM:
        print("\n")
        print(f"PLAYER {SYM} WILL BE WIN ......!!!!")
        print("\n")
        return True
    
    elif board[2][0] == board[2][1] == board[2][2] == SYM:
        print("\n")
        print(f"PLAYER {SYM} WILL BE WIN ......!!!!")
        print("\n")
        return True
    
    elif board[0][0] == board[1][0] == board[2][0] == SYM:
        print("\n")
        print(f"PLAYER {SYM} WILL BE WIN ......!!!!")
        print("\n")
        return True
    
    elif board[0][1] == board[1][1] == board[2][1] == SYM:
        print("\n")
        print(f"PLAYER {SYM} WILL BE WIN ......!!!!")
        print("\n")
        return True
    
    elif board[0][2] == board[1][2] == board[2][2] == SYM:
        print("\n")
        print(f"PLAYER {SYM} WILL BE WIN ......!!!!")
        print("\n")
        return True
    
    elif board[0][0] == board[1][1] == board[2][2] == SYM:
        print("\n")
        print(f"PLAYER {SYM} WILL BE WIN ......!!!!")
        print("\n")  
        return True
          
    elif board[0][2] == board[1][1] == board[2][0] == SYM:
        print("\n")
        print(f"PLAYER {SYM} WILL BE WIN ......!!!!")
        print("\n")
        return True
    

def placement(number):
    if(number == 1):
        return [0,0]

    if(number == 2):
        return [0,1]

    if(number == 3):
        return[0,2]

    if(number == 4):
        return[1,0]

    if(number == 5):
        return [1,1]
    
    if(number == 6):
        return[1,2]

    if(number == 7):
        return[2,0]

    if(number == 8):
        return[2,1]

    if(number == 9):
        return[2,2]
    

def board_is_full(board,SYM):

    if(SYM == 'X'):
        count_X=0
        for i in range(0,3):
            for j in range(0,3):
                if(board[i][j]=='X'):
                    count_X += 1
        if(count_X==3):
            return True
        
    elif(SYM == 'Y'):
        count_Y=0
        for i in range(0,3):
            for j in range(0,3):
                if(board[i][j]=='Y'):
                    count_Y += 1
        if(count_Y==3):
            return True
    
    return False


def display(arr):
    for i in range(0,3):
        print("                            ")
        print(f"{arr[i][0]}       |     {arr[i][1]}      |      {arr[i][2]}     ")


def player_movers(SYM,board):
    
    counter = 0
    while(counter<10):
        
        place = int(input(f"playing player_{SYM} , enter block no. (1-9) : "))
        print("\n")
        value = placement(place)
    
        if(board[value[0]] [value[1]] == 0):
            board [value[0]] [value[1]] =SYM
            counter = 10
        else:
            
            print("Thar place is already filled, choose another")
            print("\n")
            counter += 1
    display(board)
    print("\n")
    


def replacement(board, SYM):    
    counter = 0
    while counter < 10:
        
        old = int(input(f"Playing player_{SYM}, enter a no of replacement box : ")) 
        print("\n")
        value_old = placement(old)
        
        new = int(input(f"Which Block is assigned for that Block : "))
        print("\n")
        value_new = placement(new)
        
        if (board[value_old[0]][value_old[1]] == SYM and board[value_new[0]][value_new[1]] == SYM):
            board[value_old[0]][value_old[1]] = 0
            board[value_new[0]][value_new[1]] = SYM
            counter = 10
            break

        elif (board[value_new[0]][value_new[1]] == 0 and board[value_old[0]][value_old[1]] == SYM):
            board[value_old[0]][value_old[1]] = 0
            board[value_new[0]][value_new[1]] = SYM
            counter = 10
            break

        else:
            print("Thats not a right choice")
            print()
    display(board)
    print("\n")
  




board = [[0,0,0],
         [0,0,0],
         [0,0,0]]




print("\n")
display(board)
print("\n")

player = 1
cond = False
while(True):
    if(player==1):
        SYM='X'
        player = player + 1
        check = condition(board,SYM)
        if(board_is_full(board,SYM) == True):
            replacement(board,SYM)
            check=condition(board,SYM)
        else:
            player_movers(SYM,board)
            check= condition(board,SYM)
            
    elif(player==2):
        SYM = 'Y'
        player = player - 1
        
        check=condition(board,SYM)
        if(board_is_full(board,SYM) == True):
            replacement(board,SYM)
            check=condition(board,SYM)
        else:
            player_movers(SYM,board)
            check=condition(board,SYM)

    if(check==True):
        print("THANKS FOR PLAYING THE GAME......!!!!\nVisit Again....")
        break
