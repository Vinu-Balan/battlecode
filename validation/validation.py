import random

# function to implement AI logicA
def LogicA(prev_moves):
    # Write your Logic here
    return 0

# function to implement AI logicB
def LogicB(prev_moves):
    # Write your Logic here
    return random.choice([0,1,2])

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
    for x in range(11):
        a = LogicA(prev_movesB)
        b = LogicB(prev_movesA)
        prev_movesA.append(a)
        prev_movesB.append(b)
        print("A move: "+str(d[prev_movesA[x]]),end=' ')
        print("B move: " + str(d[prev_movesB[x]]))
        print("A score: " + str(your_score), end=' ')
        print("B score: " + str(opp_score))
        if whowin(prev_movesA[x],prev_movesB[x])==1:
            winner = "A Won"
            your_score+=1
        elif whowin(prev_movesA[x],prev_movesB[x])==0:
            opp_score+=1
            winner = "B Won"
        else:
            winner = "Match Draw"
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