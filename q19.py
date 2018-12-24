def addr(registry,op):
    registry[op[3]]=registry[op[1]]+registry[op[2]]
    return registry

def addi(registry,op):
    registry[op[3]]=registry[op[1]]+op[2]
    return registry

def mulr(registry,op):
    registry[op[3]]=registry[op[1]]*registry[op[2]]
    return registry

def muli(registry,op):
    registry[op[3]]=registry[op[1]]*op[2]
    return registry

def banr(registry,op):
    registry[op[3]]=registry[op[1]] & registry[op[2]]
    return registry

def bani(registry,op):
    registry[op[3]]=registry[op[1]] & op[2]
    return registry

def borr(registry,op):
    registry[op[3]]=registry[op[1]]|registry[op[2]]
    return registry

def bori(registry,op):
    registry[op[3]]=registry[op[1]]|op[2]
    return registry

def setr(registry,op):
    registry[op[3]]=registry[op[1]]
    return registry

def seti(registry,op):
    registry[op[3]]=op[1]
    return registry

def gtir(registry,op):
    registry[op[3]]=1 if op[1]>registry[op[2]] else 0
    return registry

def gtri(registry,op):
    registry[op[3]]=1 if registry[op[1]]>op[2] else 0
    return registry

def gtrr(registry,op):
    registry[op[3]]=1 if registry[op[1]]>registry[op[2]] else 0
    return registry

def eqir(registry,op):
    registry[op[3]]=1 if op[1]==registry[op[2]] else 0
    return registry

def eqri(registry,op):
    registry[op[3]]=1 if registry[op[1]]==op[2] else 0
    return registry

def eqrr(registry,op):
    registry[op[3]]=1 if registry[op[1]]==registry[op[2]] else 0
    return registry


opcodes={}
opcodes["addr"]=addr
opcodes["addi"]=addi
opcodes["mulr"]=mulr
opcodes["muli"]=muli
opcodes["banr"]=banr
opcodes["bani"]=bani
opcodes["borr"]=borr
opcodes["bori"]=bori
opcodes["setr"]=setr
opcodes["seti"]=seti
opcodes["gtir"]=gtir
opcodes["gtri"]=gtri
opcodes["gtrr"]=gtrr
opcodes["eqir"]=eqir
opcodes["eqri"]=eqri
opcodes["eqrr"]=eqrr

ip=5
registery = [1,0,0,0,0,0]
#registery = [0, 0, 10551430, 10551430, 1, 9]
#registery = [10551430, 0, 10551430, 10551429, 1, 15]

#10551431
qty=0
with open('data/q19.txt', 'r') as content_file:
    content = content_file.read()


app=[]
for line in content.split("\n"):
    op=line.split(" ")
    for i in range(1,len(op)):
        op[i]=int(op[i])
    app.append(op)

#execute
while registery[ip]>=0 and registery[ip] < len(app):
    op = app[registery[ip]]
    registery=opcodes[op[0]](registery.copy(),op)
    registery[ip]+=1
    #if qty%7==0:
    print(qty,": ",registery)
    input()

    qty+=1

print(registery)