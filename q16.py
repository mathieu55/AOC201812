import operator

class testSuite():
    def __init__(self):
        self.tests=[]

    def testAllByTest(self, fcts):
        results=[]
        for _ in range(len(self.tests)):
            results.append([])

        for i in range(len(self.tests)):
            for func in fcts:
                fctReturn=func(self.tests[i].before.copy(),self.tests[i].action)
                if (fctReturn>self.tests[i].after)-(fctReturn<self.tests[i].after)==0:
                    results[i].append(func)
        return results

    def testAllByFunc(self, fcts):
        results=[]
        for _ in range(len(fcts)):
            tmp=[]
            results.append(tmp)
            for _ in range(len(fcts)):
                tmp.append(0)

        for test in self.tests:
            for i,func in enumerate(fcts):
                fctReturn=func(test.before.copy(),test.action)
                if (fctReturn>test.after)-(fctReturn<test.after)==0:
                    results[test.action[0]][i]+=1
        return results

class testCase():
    def __init__(self,pAction, valueBefore, valueAfter):
        self.action=pAction
        self.before=valueBefore
        self.after=valueAfter

    def __repr__(self):
        return "Op: "+str(self.action)+"\nBefore: "+str(self.before)+"\nAfter: "+str(self.after)

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

opcodes=[addr,addi,mulr,muli,banr,bani,borr,bori,setr,seti,gtir,gtri,gtrr,eqir,eqri,eqrr]

with open('data/q16.txt', 'r') as content_file:
    content = content_file.read()

lines = content.split("\n")
emptyLine=0
i=0

tests = testSuite()
while emptyLine<=1: #and len(tests.tests)<=10:
    tmpLine=lines[i]
    if tmpLine=="":
        emptyLine+=1
    else:
        emptyLine=0
        before=list(map(lambda x: int(x.strip()),tmpLine[9:-1].split(",")))
        
        i+=1
        tmpLine=lines[i]
        action=list(map(lambda x: int(x.strip()),tmpLine.split(" ")))
        
        i+=1
        tmpLine=lines[i]
        after=list(map(lambda x: int(x.strip()),tmpLine[9:-1].split(",")))        
        tests.tests.append(testCase(action,before,after))  
        pass
    i+=1

#skip white line
while lines[i].strip()=="":
    i+=1

#execute the "software"
values=[0,0,0,0]
indexOpcode=[8,15,11,3,13,6,7,2,12,9,4,14,0,10,1,5]
while i<len(lines):
    op=list(map(lambda x: int(x.strip()),lines[i].split(" ")))
    opcodes[indexOpcode[op[0]]](values,op)
    i+=1

print(values)
