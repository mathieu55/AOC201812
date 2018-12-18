

with open('data/q15.txt', 'r') as content_file:
    content = content_file.read().strip()

plan=[]
for line in content.split("\n"):
    tmp=[]
    plan.append(tmp)
    for char in line:
        tmp.append(char)


