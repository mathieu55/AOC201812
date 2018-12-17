inputPuzzle=3031
maxX=300
maxY=300

class fuelCell:
    def __init__(self, posX, posY, gridSerialNumber):
        self.x=posX
        self.y=posY
        self.rackId=posX+10
        self.gridSerial=gridSerialNumber

        self.power=(self.rackId*posY+self.gridSerial)*self.rackId
        if self.power>=100:
            self.power=int(str(self.power)[-3:-2])
        else:
            self.power=0
        self.power-=5

gridd=[]
for i in range(maxY):
    gridd.append([])
    for k in range(maxX):
        gridd[i].append(fuelCell(k+1,i+1,inputPuzzle))

iMax=None
powerMax=-10000000

for size in range(len(gridd)):
    print("size",size)
    for i in range(len(gridd)-size):
        for k in range(len(gridd[i])-size):
            sumCell=0
            for iCell in range(size+1):
                for kCell in range(size+1):
                    sumCell+=gridd[i+iCell][k+kCell].power
            if sumCell > powerMax:
                powerMax=sumCell
                iMax=(k+1,i+1,size+1)
    print("Max, size:",powerMax)
    print("Coord:",iMax)

print("Max:",powerMax)
print("Coord:",iMax)

