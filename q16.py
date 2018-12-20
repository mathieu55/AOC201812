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



class testCase():
    def __init__(self,pAction, valueBefore, valueAfter):
        self.action=pAction
        self.before=valueBefore
        self.after=valueAfter

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
    registry[op[3]]=1 if op[1]>registry[op[2]] else 0
    return registry

def eqri(registry,op):
    registry[op[3]]=1 if registry[op[1]]>op[2] else 0 
    return registry

def eqrr(registry,op):
    registry[op[3]]=1 if registry[op[1]]>registry[op[2]] else 0
    return registry

opcodes=[addr,addi,mulr,muli,banr,bani,borr,bori,setr,seti,gtir,gtri,gtrr,eqir,eqri,eqrr]

with open('data/q16.txt', 'r') as content_file:
    content = content_file.read()

lines = content.split("\n")
emptyLine=0
i=0

tests = testSuite()
while emptyLine<=1:
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
    
results=tests.testAllByTest(opcodes)
qty=[len(i) for i in results]
qty3more = list(filter(lambda i: i>=3,qty))
#465 too low

print(len(qty3more))