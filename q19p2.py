#Convert hint into a common app
#r2=10551430
#for r4=1;r4<=r2;r4++:
#    for r3=1; r3<=r2; r3++:
#        if r4*r3 == r2:
#            r0+=r4

hint=10551430
mults=[]

for i in range(1,hint+1):
    if hint % i == 0:
        mults.append(i)

print("Mults:",mults)
total=0
for mult in mults:
    total+=mult

print("Total:",total)