import re

#Split the words based on the vowels
def vowels():
    list = open("rakul.txt", 'r')
    list1=[]
    for line in list:
         string = re.sub("[^0-9a-zA-Z]", " ",line).split(" ")
         for word in string:
             if(word!=""):
               list1.append(word)
    res=[re.sub("[aeiouAEIOU]",' ',i) for i in list1]
    return str(res)

# Use – in place of blank space
def hyphen():
    list = open("rakul.txt", 'r')
    list1=[]
    for line in list:
        string=line.replace(" ","-")
        list1.append(string)
    return str(list1)

#Use semicolon instead of newline
def semi():
    list = open("rakul.txt", 'r')
    string = list.read()
    res = string.replace("\n",";")
    return str(res)

#Capitalize 3rd word
def caps3():
    words = open("rakul.txt", 'r')
    cap = []
    for i in words:
        a = list(i)
        a[2::3] = [x.upper() for x in a[2::3]]
        i = ''.join(a)
        cap.append(i)
    return str(cap)

#Capitalize 5th word
def Caps5():
    words = open("rakul.txt", 'r')
    Line = words.readlines()
    for line in Line:
        string = re.sub("[^a-zA-Z0-9]", " ", line).split(" ")
        for i in range(4, len(string), 5):
            string[i] = string[i].upper()
        return string
#reverse function to check palindrome
def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str

#maxi function to check maximum element
def maxi():
    count = 0
    word = ""
    maxCount = 0
    words = []
    file = open("rakul.txt", "r")
    for line in file:
        # string = line.lower().replace(',', '').replace('.', '').split(" ")
        string = re.sub("[^A-Za-z0-9]"," ",line).split(" ")
        for s in string:
            words.append(s)
    for i in range(0, len(words)):
        count = 1
        for j in range(i + 1, len(words)):
            if (words[i] == words[j]):
                count = count + 1
        if (count > maxCount):
            maxCount = count;
            word = words[i];
    return word

maximum=maxi()
vowel=vowels()
hyphen=hyphen()
semi=semi()
caps3=caps3()
Caps5=Caps5()
#different list of To, Ing, Palindrome, All unique words
to=[]
ing=[]
palindrome=[]
result=[]
count1=0
count2=0
#opening file
file=open("rakul.txt","r")
#iterating and adding words to file
for line in file:
    arr=line.split()
    for i in arr:
        if i.startswith("To"):
            count1+=1
        if i.endswith("ing"):
            count2+=1
        if reverse(i) == i:
            palindrome.append(i)
        result.append(i)
to.append(count1)
ing.append(count2)
res=enumerate(result)

#writing words to file
with open('filenew.txt', 'w+') as f:
    f.write("# To words:\n=>")
    f.write(str(to))
    f.write("\n\n# Ing words:\n=>")
    f.write(str(ing))
    f.write("\n\n# Maximum occured word: \n=>%s"% maximum)
    f.write("\n\n# Palindrome words:\n=>")
    f.write(str(palindrome))
    f.write("\n\n# Key value pairs:\n=>")
    f.write(str(list(res)))
    f.write("\n\n# Splitting vowels of each word:\n=>")
    f.write(str(vowel))
    f.write("\n\n# Use - in place of blank space:\n=>")
    f.write(str(hyphen))
    f.write("\n\n# Use semicolon instead of newline:\n=>")
    f.write(str(semi))
    f.write("\n\nCapitalized every 3rd word: \n=>")
    f.write(str(caps3))
    f.write("\n\nCapitalized every 5th word: \n=>")
    f.write(str(Caps5))
    print(">>Text written to filenew.txt..Check it!!")
f.close()

#printing unique list that contains all words
print("# Printing unique list that contains all words\n=>",result)
