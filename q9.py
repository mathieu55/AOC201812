import operator
#411 players; last marble is worth 72059 points

class node:
    def __init__(self, id):
        self.id=id
        self.before=None
        self.after=None
        self.isRetire=False
        pass

    def insert(self,item,insertBefore=False):
        nodeBefore=self
        nodeAfter=self.after
        if insertBefore:
            nodeBefore=self.before
            nodeAfter=self

        node.insertBetween(item,nodeBefore,nodeAfter)

    def retire(self):
        if not(self.before is None):
            self.before.after=self.after

        if not(self.after is None):
            self.after.before=self.before

        self.after=None
        self.before=None
        self.isRetire=True
        return self

    @staticmethod
    def insertBetween(item, before, after):
        item.before=before
        item.after=after

        if not (before is None):
            before.after=item

        if not (after is None):
            after.before = item

def play(qtyPlayer,lastmMarble):
    currentPlayer=-1
    isBefore=True
    iCurrentMarble=0
    allMarble=[]
    playerMarbles=[]
    for _ in range(qtyPlayer):
        playerMarbles.append([])


    for iMarble in range(lastmMarble+1):
        tmpMarble = node(iMarble)
        allMarble.append(tmpMarble)
        currentMarble = allMarble[iCurrentMarble]

        if iMarble > 0 :
            if iMarble % 23 == 0:
                playerMarbles[currentPlayer].append(tmpMarble)
                tmpMarble.isRetire=True

                newCurrentMarble = currentMarble
                for _ in range(7):
                    newCurrentMarble = newCurrentMarble.before

                iCurrentMarble=newCurrentMarble.id
                playerMarbles[currentPlayer].append(newCurrentMarble.before.retire())
            else:
                currentMarble.insert(tmpMarble,isBefore)

        printState(iMarble,allMarble[0],iCurrentMarble)

        currentPlayer=(currentPlayer+1)%qtyPlayer
        isBefore=not isBefore
        if isBefore:
            iCurrentMarble+=1
            while allMarble[iCurrentMarble].isRetire:
                iCurrentMarble+=1



    return playerMarbles

def HightScore(scores):
    scoreByPlayer = []
    for player in scores:
        score=0
        for marble in player:
            score+=marble.id
        scoreByPlayer.append(score)


    index, highscore = max(enumerate(scoreByPlayer), key=operator.itemgetter(1))

    print("Player:",index+1," Highscore:", highscore)

    return (index+1,highscore)

def printState(step, state, current=-1):
    strState="["+"{:3d}".format(step)+"]"

    tmpState=state
    while not (tmpState.before is None):
        tmpState=tmpState.before

    while not (tmpState is None):

        if current == tmpState.id:
            strState+="{:3d}".format(tmpState.id)+"*"
        else:
            strState+=("{:4d}".format(tmpState.id))

        tmpState=tmpState.after

    print(strState)

assert HightScore(play(7,25))[1]==32,"Test fail 0"
#assert HightScore(play(10,1618))[1]==8317,"Test fail 1"
#assert HightScore(play(13,7999))[1]==146373,"Test fail 2"
#assert HightScore(play(17,1104))[1]==2764,"Test fail 3"
#assert HightScore(play(21,6111))[1]==54718,"Test fail 4"
#assert HightScore(play(30,5807))[1]==37305,"Test fail 5"

#printScore(play(411, 72059))
