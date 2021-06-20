import re
rakul=set({})
file=open("rakul.txt","r")

for line in file:
    string = re.sub("[^A-Za-z0-9]"," ",line).split(" ")
    for s in string:
        if s!="":
          p=len(s)
          rakul.add(str(p)+s)
l=list(sorted(rakul))
with open('filenew.txt', 'w+') as f:
    for items in l:
        f.write('%s ' % items)
    print("Text written to filenew.txt..Check it!!")
f.close()