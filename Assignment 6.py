game_board = [["-","-","-"],["-","-","-"],["-","-","-"]]    
i=0;j=0;R=0
def show():                   
 for row in game_board:
    for cel in row:
        print(cel,end="  ")
    print()   
while True:
    if R<9 :
        print("player 1")
        while True:
            
            row = int(input("Enter row:"))
                            
            col = int(input("enter col:"))
            if 0<=row<=2 and 0<=col<=2:
                if game_board[row][col]=="-":      
                    game_board[row][col]="X"
                    R=R+1
                    show()
                    break
                    
                else:
                    print("Ye khone digar entekhab kon:")
                    break
                
                    
            else:
                print("beyn 0 ta 2 mituni entekhab koni:")
                break
        print("player 2")
        while True:
            row = int(input("enter row:"))
            col = int(input("enter col:"))
            if 0<=row<=2 and 0<=col<=2:


                if game_board[row][col]=="-":      
                    game_board[row][col]="0"
                    R=R+1
                    show()
                    break
                else  :
                    print("Ye khone digar entekhab kon:")
                    break
                    
            else:

                print("beyn 0 ta 2 mituni entekhab koni:")
                break
        while True:
            if game_board[0][0]=="X" and game_board[0][1]=="X" and game_board[0][2]=="X" and i<1: 
                i=i+1
                print("bazikon aval barande shod!!")
                break
                
            elif game_board[1][0]=="X" and game_board[1][1]=="X" and game_board[1][2]=="X" and i<1:
                i=i+1
                print("bazikon aval barande shod!!")
                break
            elif game_board[2][0]=="X" and game_board[2][1]=="X" and game_board[2][2]=="X" and i<1:    
                i=i+1
                print("bazikon aval barande shod!!")
                break
            elif  game_board[0][0]=="X" and game_board[1][0]=="X" and game_board[2][0]=="X" and i<1: 
                i=i+1
                print("bazikon aval barande shod!!")
                break    
            elif game_board[0][1]=="X" and game_board[1][1]=="X" and game_board[2][1]=="X" and i<1:
                i=i+1
                print("bazikon aval barande shod!!")
                break
            elif game_board[0][2]=="X" and game_board[1][2]=="X" and game_board[2][2]=="X" and i<1:
                i=i+1
                print("bazikon aval barande shod!!")
                break
            elif game_board[0][0]=="X" and game_board[1][1]=="X" and game_board[2][2]=="X" and i<1:
                i=i+1
                print("bazikon aval barande shod!!")
                break
            elif game_board[0][2]=="X" and game_board[1][1]=="X" and game_board[2][0]=="X" and i<1:
                i=i+1
                print("bazikon aval barande shod!!")
                break
            if game_board[0][0]=="0" and game_board[0][1]=="0" and game_board[0][2]=="0" and j<1:  
                j=j+1
                print("bazikon dovom barande shod!!")
                break
            elif game_board[1][0]=="0" and game_board[1][1]=="0" and game_board[1][2]=="0" and j<1:
                j=j+1
                print("bazikon dovom barande shod!!")
                break
            elif game_board[2][0]=="0" and game_board[2][1]=="0" and game_board[2][2]=="0" and j<1:
                i=i+1
                print("bazikon dovom barande shod!!") 
                break
            elif  game_board[0][0]=="0" and game_board[1][0]=="0" and game_board[2][0]=="0" and j<1: 
                j=j+1
                print("bazikon dovom barande shod!!")
                break
            elif game_board[0][1]=="0" and game_board[1][1]=="0" and game_board[2][1]=="0" and j<1:
                j=j+1
                print("bazikon dovom barande shod!!")
                break
            elif  game_board[0][2]=="0" and game_board[1][2]=="0" and game_board[2][2]=="0" and j<1:
                j=j+1
                print("bazikon dovom barande shod!!")
                break
            elif game_board[0][0]=="0" and game_board[1][1]=="0" and game_board[2][2]=="0" and j<1:
                j=j+1
                print("bazikon dovom barande shod!!")
                break 
            elif game_board[0][2]=="0" and game_board[1][1]=="0" and game_board[2][0]=="0" and j<1:
                j=j+1
                print("bazikon dovom barande shod!!")
                break
            else:
                break
    else :
        print("finish")
        break

if i>j :
    
    print("player 1 wins")
    
        
elif j>i :
    print("player 2 wins")
    

elif i==j:
    print("both of them are equal")


