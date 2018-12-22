from PIL import Image, ImageDraw

class coord():
    def __init__(self,data=""):
        if data == "":
            return

        tmp = sorted(data.replace(" ","").split(","))

        self.x= list(map(lambda obj: int(obj.strip()),tmp[0].split("=")[1].split("..")))
        self.y= list(map(lambda obj: int(obj.strip()),tmp[1].split("=")[1].split("..")))

        if len(self.x)==1:
            self.x.append(self.x[0])

        if len(self.y)==1:
            self.y.append(self.y[0])

        self.x[1]+=1
        self.y[1]+=1

    def __repr__(self):
        return "<coord x="+str(self.x)+" y="+str(self.y)+">"

def moveWater(source):
    water=(source[0],source[1]+1)

    while water[1]<len(plan) and plan[water[1]][water[0]]=="":
        plan[water[1]][water[0]]="|"
        water=(water[0],water[1]+1)

    if water[1]>=len(plan) or plan[water[1]][water[0]]=="|":
        return
    else:
        #bucket is full check other layer
        while fillWithWater(water):
            water=(water[0],water[1]-1)



def fillWithWater(source,direction=0,waterType="|"):
    if direction==0:
        if plan[source[1]][source[0]]=="" and plan[source[1]+1][source[0]]=="~":
            plan[source[1]][source[0]]="|"
        right = fillWithWater(source,1,waterType)
        left = fillWithWater(source,-1,waterType)
        if waterType=="|" and right and left:
            fillWithWater(source,1,"~")
            fillWithWater(source,-1,"~")
            if plan[source[1]][source[0]]!="#":
                plan[source[1]][source[0]]="~"
        return right and left
    else:
        x=source[0]+direction
        y=source[1]

        while plan[y][x] != "#" and y+1<len(plan) and plan[y+1][x] != "" and plan[y+1][x] != "|":
            plan[y][x]=waterType
            x+=direction

        if plan[y][x] == "#":
            return True
        else:
            plan[y][x]=waterType
            if y+1<len(plan) and plan[y+1][x] == "":
                moveWater((x,y))
            return False

def createImage(width,height):
    picture = Image.new("RGB",(width,height),(255,255,255))
    pDraw = ImageDraw.Draw(picture)
    for y in range(len(plan)):
        for x in range(len(plan[y])):
            tile=plan[y][x]
            tileColor = (255,255,255)
            if tile == "#":
                tileColor = (126,52,57)
            elif tile == "~":
                tileColor = (0,0,255)
            elif tile == "|":
                tileColor = (15,179,240)

            pDraw.point((x,y),tileColor)
    picture.save("out/q17.bmp")

with open('data/q17.txt', 'r') as content_file:
    content = content_file.read().strip()

coords = [coord(line) for line in content.split("\n")]

#get plan dimension
minX = min(coords,key=lambda icoord:icoord.x[0]).x[0]
maxX = max(coords,key=lambda icoord:icoord.x[1]).x[1]+6
minY = min(coords,key=lambda icoord:icoord.y[0]).y[0]
maxY = max(coords,key=lambda icoord:icoord.y[1]).y[1]

#Prepare plan
plan=[]
for y in range(maxY):
    tmp=[]
    plan.append(tmp)
    for x in range(maxX):
        tmp.append("")

#set clay tile
for icoord in coords:
    for y in range(icoord.y[0],icoord.y[1]):
        for x in range(icoord.x[0],icoord.x[1]):
            plan[y][x]="#"

moveWater((500,0))

#clean solution
for y in range(len(plan)):
    for x in range(len(plan[y])):
        if plan[y][x]=="|" and plan[y-1][x]=="~":
            plan[y][x]="~"

createImage(maxX,maxY)

sum=0
for y in range(minY,maxY):
    sum+=len(list(filter(lambda xValue: xValue in ["~"],plan[y])))

print("sum: ",sum)