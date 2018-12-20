with open('data/q16.txt', 'r') as content_file:
    content = content_file.read().strip()

class testSuite():
    def __init__(self):
        self.tests=[]

    def testAll(self, fcts):
        results=[]
        for _ in range(len(fcts)):
            results.append([])

        return results

class testCase():
    def __init__(self,pAction, valueBefore, valueAfter):
        self.action=pAction
        self.before=valueBefore
        self.after=valueAfter

line = content.split("\n")
emptyLine=0
i=0
while emptyLine<=1:
    
    pass
    