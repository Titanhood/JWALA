#question_1
a=open("naruto.txt")
lines=[]
b=int(input("Lines "))
for i in range(0,b):
    line=a.readline()
    print(line)
#question_2
a=open('naruto.txt')
lines=a.readlines()
wors=[]
count=[]
for l in lines:
    words=l.split()
    wors=wors+words
print(wors)
Wrd=set(wors)
for i in Wrd:
    cnt=0
    for j in wors:
        if i==j:
            cnt=cnt+1
    count.append(cnt)
wrds=list(Wrd)
for i in range(0,len(wrds)):
    print("The Count of {} is :{}".format(wrds[i],count[i]))
#question_3
f=open('naruto.txt')
F=open('naruto2.txt','w')
f_data=f.read()
F.write(f_data)
f.close()
F.close()
#question_4
x = open('naruto.txt', 'r+')
y = open('naruto2.txt', 'r+')
z = open('naruto3.txt', 'w')
lines = x.readlines()
lines1 = y.readlines()
lines2 = list()
print(lines)
print(lines1)
if len(lines) > len(lines1):
    for i in range(0, len(lines1)):
        lines2.append(lines[i] + lines1[i])
    for i in range(len(lines1), len(lines)):
        lines2.append(lines[i])
else:
    for i in range(0, len(lines)):
        lines2.append(lines[i] + lines1[i])
    for i in range(len(lines), len(lines1)):
        lines2.append(lines1[i])
for i in range(0, len(lines2)):
    lines2[i] = lines2[i].replace('\n', ' ')
    z.writelines(lines2[i] + '\n')
x.close()
y.close()
z.close()
#question_5
f=open('naruto4.txt')
g=open('naruto5.txt','w')
lines=f.readlines()
print(lines)
for i in range(0,len(lines)):
    lines[i]=int(lines[i])
lines=sorted(lines)
for i in range(0,len(lines)):
    lines[i]=str(lines[i])
    g.writelines(lines[i]+'\n')
