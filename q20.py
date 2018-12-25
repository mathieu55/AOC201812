from collections import defaultdict
from PIL import Image, ImageDraw

class dongeon():

    plan=defaultdict(defaultdict)

    moves = {}
    moves["N"]=(0,-1,"-")
    moves["S"]=(0,1,"-")
    moves["E"]=(1,0,"|")
    moves["W"]=(-1,0,"|")

    @staticmethod
    def printWorld():
        minY = min(dongeon.plan.keys())
        maxY = max(dongeon.plan.keys())

        minX=99999999999999
        maxX=-99999999999999
        for line in dongeon.plan.values():
            minX = min([minX,min(line.keys() or [minX])])
            maxX = max([maxX,max(line.keys() or [maxX])])

        for y in range(minY-1,maxY+2):
            row = ""
            for x in range(minX-1,maxX+2):
                tile = dongeon.plan[y].get(x,"#")

                row+=tile
            print(row)


    def __init__(self, iterChar, coord):
        self.iterChar = iterChar
        self.coord=coord
        self.paths=[]

        char=""
        currentPath=""
        currentCoord=(coord[0],coord[1])
        char=next(iterChar)
        while not (char in ["$",")"] ):
            if char=="^":
                dongeon.plan[0][0]="X"
            elif char=="|":
                self.paths.append(currentPath)
                currentPath=""
                currentCoord=coord
            elif char=="(":
                self.paths.append(dongeon(iterChar,currentCoord))
            else:
                move = dongeon.moves[char]
                currentCoord=(currentCoord[0]+move[0],currentCoord[1]+move[1])
                dongeon.plan[currentCoord[1]][currentCoord[0]]=move[2]
                currentCoord=(currentCoord[0]+move[0],currentCoord[1]+move[1])
                dongeon.plan[currentCoord[1]][currentCoord[0]]="."
                currentPath+=char

            char=next(iterChar)

        self.paths.append(currentPath)



with open('data/q20.txt', 'r') as content_file:
    content = content_file.read().strip()

#content="^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$" #23
#content="^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$"  #31


iChar = iter(content)
world = dongeon(iChar,(0,0))

#min max
minY = min(dongeon.plan.keys())
maxY = max(dongeon.plan.keys())

minX=99999999999999
maxX=-99999999999999
for line in dongeon.plan.values():
    minX = min([minX,min(line.keys())])
    maxX = max([maxX,max(line.keys())])
minX-=1
minY-=1

maxX+=1
maxY+=1

im = Image.new("RGB",(maxX-minX+1,maxY-minY+1),(255,255,255))
imDraw = ImageDraw.Draw(im)

#find the fartess room
todos=[(0,0)]
done={}
distance=0
doors=[]
while len(todos)>0:
    newTodos=[]
    for todo in todos:
        done[todo]=distance
        for move in dongeon.moves.values():
            door=(todo[0]+move[0],todo[1]+move[1])
            room=(door[0]+move[0],door[1]+move[1])
            if dongeon.plan[door[1]].get(door[0],"#") in ["|","-"]:
                if not (room in done.keys()) and not(room in newTodos) :
                    newTodos.append(room)
                    doors.append(door)
    distance+=1
    todos=newTodos
    newTodos=None

maxLenght = max(done.values())
print("Lenght:", maxLenght)

colors={"#":(0,0,0), "X":(255,0,0), "-":(255,255,255), "|":(255,255,255), ".":(255,255,255)}

for y in range(minY, maxY):
    for x in range(minX,maxX):
        tile=dongeon.plan[y].get(x,"#")
        color=colors[tile]

        if not(x==0 and y==0) and ((x,y) in doors or (x,y) in done.keys()):
            color=(0,255,0)

        imDraw.point((x-minX,y-minY),color)

im.save("out/q20.bmp")

#dongeon.printWorld()

room1000 = len(list(filter(lambda distance:distance>=1000,done.values())))
print("room 1000: ",room1000)