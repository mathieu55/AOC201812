class plan:

    plan=[]
    def __init__(self, strPlan=None):
        
        self.karts=[]
        self.tick=0
        self.crashes=[]
        
        if strPlan is None:
            return

        y=0
        for line in strPlan.split("\n"):
            tmp=[]
            self.plan.append(tmp)
            x=0
            for char in line:
                if char in kart.directions:
                    self.karts.append(kart(x,y,char))
                    if char in ["<",">"]:
                        tmp.append("-")
                    else:
                        tmp.append("|")
                else:
                    tmp.append(char)
                x+=1
            y+=1

    def moveAll(self):
        for iKart in self.karts:
            iKart.move()
        hasCrash=self.detectCrash()
        self.tick+=1
        return hasCrash

    def detectCrash(self):
        toRemove=[]
        hasCrash=False
        for i in range(len(self.karts)-1):
            for k in range(len(self.karts)-i-1):
                k2=k+i+1
                if self.karts[i].x == self.karts[k2].x and self.karts[i].y == self.karts[k2].y:
                    self.crashes.append((self.karts[i].x,self.karts[i].y,self.tick))
                    
                    toRemove.append(self.karts[i])
                    toRemove.append(self.karts[k2])
                    hasCrash= True

        for item in toRemove:
            try:
                self.karts.remove(item)
            except ValueError:
                pass

        return hasCrash

class kart:
    directions=["^",">","v","<"]
    moveByDirection={}
    moveByDirection["^"]=(0,-1)
    moveByDirection["v"]=(0,1)
    moveByDirection[">"]=(1,0)
    moveByDirection["<"]=(-1,0)
    
    directionByTile={}
    directionByTile[("|","^")]="^"
    directionByTile[("|","v")]="v"
    directionByTile[("|",">")]=None
    directionByTile[("|","<")]=None

    directionByTile[("-","^")]=None
    directionByTile[("-","v")]=None
    directionByTile[("-",">")]=">"
    directionByTile[("-","<")]="<"
    
    directionByTile[("/","^")]=">"
    directionByTile[("/","v")]="<"
    directionByTile[("/",">")]="^"
    directionByTile[("/","<")]="v"

    directionByTile[("\\","^")]="<"
    directionByTile[("\\","v")]=">"
    directionByTile[("\\",">")]="v"
    directionByTile[("\\","<")]="^"

    directionByTile[("left","^")]="<"
    directionByTile[("left","v")]=">"
    directionByTile[("left",">")]="^"
    directionByTile[("left","<")]="v"

    directionByTile[("straight","^")]="^"
    directionByTile[("straight","v")]="v"
    directionByTile[("straight",">")]=">"
    directionByTile[("straight","<")]="<"

    directionByTile[("right","^")]=">"
    directionByTile[("right","v")]="<"
    directionByTile[("right",">")]="v"
    directionByTile[("right","<")]="^"

    turns=["left","straight","right"]
    
    def __init__(self,posX,posY,kartDirection):
        self.x=posX
        self.y=posY
        self.direction=kartDirection
        self.iTurn=0

    def move(self):
        step=kart.moveByDirection[self.direction]
        self.x+=step[0]
        self.y+=step[1]
        tile=plan.plan[self.y][self.x]
        if tile=="+":
            tile=kart.turns[self.iTurn]
            self.iTurn=(self.iTurn+1)%len(kart.turns)

        self.direction=kart.directionByTile[(tile,self.direction)]



with open('data/q13.txt', 'r') as content_file:
    content = content_file.read()

tracks = plan(content)

while len(tracks.karts)!=1:
    if tracks.moveAll():
        print("Crash:",tracks.crashes[len(tracks.crashes)-1]," Only ",len(tracks.karts)," left")

print("survivor: (",tracks.karts[0].x,",",tracks.karts[0].y,")")
