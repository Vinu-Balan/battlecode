import random

# function to implement AI logicA
def LogicA(prev_moves,round_no):
    if sum(prev_moves)>4:
        temp = 2
    elif sum(prev_moves)>2:
        temp = 1
    else:
        temp = 0
    return temp

# function to implement AI logicB
def LogicB(prev_moves,round_no):
    # Write your Logic here
    l = []
    p = []
    d = {0:1,1:2,2:1}
    if len(prev_moves)==0:
        return 0
    else:
        l.append(prev_moves[-1])
        if len(l)==3:
            p = l.copy()
        return d[l[-1]]
        if len(l)>3:
            return d[p[(len(prev_moves)+1)%3]]
            
    return 0

# Driver Code
def whowin(a,b):
    if (a==0 and b==2) or (a==1 and b==0) or (a==2 and b==1):
        return 1
    elif a==b:
        return -1
    else:
        return 0
if __name__=='__main__':
    d = {0:"ROCK",1:"PAPER",2:"SISSORS"}
    prev_movesA = []
    prev_movesB = []
    your_movesA = []
    your_movesB = []
    wins = []
    your_score = 0
    opp_score = 0
    for x in range(9):
        a = LogicA(prev_movesB,x+1)
        b = LogicB(prev_movesA,x+1)
        prev_movesA.append(a)
        prev_movesB.append(b)
        print("A move: "+str(d[prev_movesA[x]]),end=' ')
        print("B move: " + str(d[prev_movesB[x]]))
        if whowin(prev_movesA[x],prev_movesB[x])==1:
            winner = "A Won"
            your_score+=1
        elif whowin(prev_movesA[x],prev_movesB[x])==0:
            opp_score+=1
            winner = "B Won"
        else:
            winner = "Match Draw"
        print("A score: " + str(your_score), end=' ')
        print("B score: " + str(opp_score))
        print(winner)
    if your_score>opp_score:
        print("-----------------------------------------------------")
        print("A Have won the Game!")
    elif opp_score>your_score:
        print("-----------------------------------------------------")
        print("B Have won the Game!")
    else:
        print("-----------------------------------------------------")
        print("Match Draw!")