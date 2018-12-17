def countPlantPot(pots,padding):
    sum=0
    i=-padding
    for pot in pots:
        if pot=="#":
            sum+=i
        i+=1
    return sum


with open('data/q12.txt', 'r') as content_file:
    content = content_file.read().strip()

initial_state=".##.##...#.###..#.#..##..###..##...####.#...#.##....##.#.#...#...###.........##...###.....##.##.##"

dictPot={}

for line in content.split("\n"):
    pot = line.split("=>")
    dictPot[pot[0].strip()]=pot[1].strip()

padding=5

generation=110 #50000000000
pot="".ljust(padding,".") + initial_state + "".ljust(padding,".")

for iGen in range(generation):
    nextGen=pot[1:2]
    padding-=1
    for i in range(len(pot)-4)  :
        nextGen+=dictPot.get(pot[i:i+5],pot[i+2:i+3])
    nextGen+=pot[-2:]+"."
    #if((iGen+1)>100):
    print("Gen ",iGen,": ",nextGen," (",countPlantPot(nextGen,padding),")", len(nextGen))
    
    pot=nextGen
  
#(x-101)*4+630 | x=50 000 000 000 = 200000000226