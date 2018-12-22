from collections import defaultdict
from PIL import Image, ImageDraw

def getStat(x,y):
    stats = defaultdict(int)
    indexes=indexAdj[y][x]
    for adjacent in indexes:
        adjX=adjacent[0]
        adjY=adjacent[1]
        stats[plan[adjY][adjX]]+=1
    return stats

def getNewValue(x,y):
    stats = getStat(x,y)
    value = plan[y][x]

    if value == ".":
        return "|" if stats["|"]>=3 else "."
    elif value == "|":
        return "#" if stats["#"]>=3 else "|"
    elif value == "#":
        return "#" if stats["#"]>=1 and stats["|"]>=1 else "."

    return ""

def getNewPlan():
    newPlan=[]
    for y in range(maxY):
        newPlan.append("".join([getNewValue(x,y) for x in range(maxX)]))
    return newPlan

def prepareIndex():
    for y in range(maxY):
        tmp=[]
        indexAdj.append(tmp)
        for x in range(maxX):
            indexes=[]
            tmp.append(indexes)
            for adj in adjacents:
                x2=x+adj[0]
                y2=y+adj[1]
                if x2>=0 and y2>=0 and x2 < maxX and y2 < maxY:
                    indexes.append((x2,y2))

def getStats():
    globalStats = defaultdict(int)
    for line in plan:
        for char in line:
            globalStats[char]+=1

    print(globalStats["#"],"*",globalStats["|"],"=",globalStats["#"]*globalStats["|"])

def createImage(id):
    img = Image.new("RGB",(maxX,maxY),(255,255,255))
    imgDraw = ImageDraw.Draw(img)

    for y in range(maxY):
        for x in range(maxX):
            imgDraw.point((x,y),colors[plan[y][x]])
    img.save("out/q18-"+str(id)+".bmp")

with open('data/q18.txt', 'r') as content_file:
    content = content_file.read().strip()

plan=[]
for line in content.split("\n"):
    plan.append(line)

colors={}
colors["."]=(255,255,255)
colors["|"]=(0,255,0)
colors["#"]=(255,0,0)

maxY=len(plan)
maxX=len(plan[0])

adjacents=[(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]

indexAdj=[]
prepareIndex()

print("calculate")
for i in range(1000000):
    for _ in range(1000):
        plan = getNewPlan()
    print(i,"/1000000")
    createImage(i)
    getStats()


print("end")
getStats()
