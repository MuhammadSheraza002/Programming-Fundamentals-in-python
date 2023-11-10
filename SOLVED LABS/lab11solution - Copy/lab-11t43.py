#  Consider a three dimensional array contains the  scores for players
#  first dimension is for match type ("test","ODI","T20")
#  second dimension is for match no (0,1,2 and 3)
#  third  dimension is for player no (0,1,2,3,4 ...,10)

#  Following is code to populate the array with suitable random values and display them.
#  Write a function to compute and display the average of babar azam in test
#  Write a function to compute and display the player wise average score of players in ODI
#  Write a function to compute and display the player wise maximum score  in T20
#  Write a function to compute and display the player  + match wise average

from random import randint
def main():
    score = [[[randint(0,99) for p in range(11)] for m in range(4)]for t in range(3)]
    matchtype = ["test","ODI","T20"]
    players = ["BABAR","RIZWAN","HAIDER","ZAMAN","ALI","AHMAD","ABID","FAWAD","HASSAN","SHAHEEN","SOHAIL"]
    suitableform(score,matchtype,players)
    print("player wise average score of players in ODI")
    ODIavrgofplayers(score,players)
    print("<------------------------------------------->")
    print("player wise maximum score  in T20")
    maxrunsint20(score,players)
    print("<------------------------------------------->")
    print("averge of BABAR AZAM in TEST")
    averageBABARinTEST(score)
    print("<------------------------------------------->")
    print("player + match wise runs in four ODIs")
    playerwithmatchwiserunsODI(score,players,matchtype)
def suitableform(score,matchtype,players):
    for t in range(3):
        print(matchtype[t])
        for m in range(4):
            print("\tmatch no",m)
            for p in range(11):
                print("\t\t",players[p],"score",score[t][m][p])
            print()
def totalscoreofteamin1stt20():
    pass
#player wise average score of players in ODI
def ODIavrgofplayers(runs,players):
    avrg = [0] * 11
    for p in range(11):
        for m in range(4):
            avrg[p] += runs[1][m][p]
    print("player name","\t","average runs")
    for p in range(11):
        print(players[p],"\t",avrg[p]/4)
def maxrunsint20(runs,player):
    max = [0] * 11
    for p in range(11):
        for m in range(4):
            max[p] += runs[2][m][p]
    maxruns = max[0]
    maxplayer = 0
    for p in range(11):
        if maxruns < max[p]:
            maxruns=max[p]
            maxplayer=p
        else:
            maxruns=maxruns
            maxplayer=maxplayer
    print("player name","\t","maximum runs")
    print(player[maxplayer],"has most runs in t20 series",maxruns)
def averageBABARinTEST(runs):
    ADD = 0
    for m in range(4):
        ADD += runs[0][m][0]
    print("BABAR AZAM has",ADD/4,"in TEST series")
def playerwithmatchwiserunsODI(runs,player,match):
    print("player name",end="\t")
    for m in range(4):
        print("match",m,end="\t")
    print()
    for p in range(11):
        print(player[p],end="\t")
        for m in range(4):
            print(runs[1][m][p],end="\t")
        print()

main()
