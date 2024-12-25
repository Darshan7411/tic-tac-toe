def board(xstate,ystate):
    zero="X" if xstate[0] else "O" if ystate[0] else 0
    one = "X" if xstate[1] else "O" if ystate[1] else 1
    two= "X" if xstate[2] else "O" if ystate[2] else 2
    three = "X" if xstate[3] else "O" if ystate[3] else 3
    four = "X" if xstate[4] else "O" if ystate[4] else 4
    five = "X" if xstate[5] else "O" if ystate[5] else 5
    six = "X" if xstate[6] else "O" if ystate[6] else 6
    seven = "X" if xstate[7] else "O" if ystate[7] else 7
    eight="X" if xstate[8] else "O" if ystate[8] else 8
    print(f"  {zero}  |  {one}  |  {two}  ")
    print("-----|-----|-----")
    print(f"  {three}  |  {four}  |  {five}  ")
    print("-----|-----|-----")
    print(f"  {six}  |  {seven}  |  {eight}  ")
    print()

def sum(a,b,c):
    return a+b+c

def checkwim(xstate,ystate):
    wins=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
        if sum(xstate[win[0]],xstate[win[1]],xstate[win[2]])==3:

            return 1
        if sum(ystate[win[0]],ystate[win[1]],ystate[win[2]])==3:

            return 0
    return -1

if __name__=="__main__":
    xstate=[0]*9
    ystate=[0]*9
    turn=True # True for x False  for y
    while True:
        board(xstate,ystate)
        if turn:
            print(" X's chance : ")
            value=int(input("pleas enter a position to place  "))
            xstate[value]=1
        else:
            print(" O's chance : ")
            value = int(input("pleas enter a position to place : "))
            ystate[value] = 1
        turn=not(turn)
        cnt=checkwim(xstate,ystate)
        if cnt!=-1:
            if checkwim(xstate,ystate)==1:
                print("x wins")
            else:
                print("O wins")
            print("Game over")
            restart=input("if want to restar pls enter YES||NO")
            if restart=="yes":
                exit()
            else:
                 break


