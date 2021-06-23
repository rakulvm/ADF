import re
import logging

logging.basicConfig(
    filename="test.log",
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s"
    )

file=""
class Parent():
    def init(self,file):
        self.file=file

    def readdata1(self):
        list= open("rakul.txt", 'r')
        Lines= list.read()
        return Lines

    def readdata(self):
        list = open("rakul.txt", 'r')
        Lines = list.readlines()
        return Lines

    def writedata(self, data):
        with open('filenew.txt', 'w+') as f:
            for i in data:
                f.write("%s"%i)
            print("Text written into the file. Check it!!")
            logging.debug("Starting with to".format())
        f.close()

class Child(Parent):
    #common method for printing the results
    def printdata(self,data):
        print(data)
    #Split the words based on the vowels
    def vowels(self):
        list = self.readdata()
        list1=[]
        for line in list:
             string = re.sub("[^0-9a-zA-Z]", " ",line).split(" ")
             for word in string:
                 if(word!=""):
                   list1.append(word)
        res=[re.sub("[aeiouAEIOU]",' ',i) for i in list1]
        self.printdata(str(res))
        output=self.writedata(str(res))

    # Use – in place of blank space
    def hyphen(self):
        list =  self.readdata()
        list1=[]
        for line in list:
            string=line.replace(" ","-")
            list1.append(string)
        self.printdata(str(list1))
        output=self.writedata(str(list1))

    #Use semicolon instead of newline
    def semi(self):
        list =  self.readdata1()
        res = list.replace("\n",";")
        self.printdata(str(res))
        output=self.writedata(str(res))

    #Capitalize 3rd word
    def caps3(self):
        words =  self.readdata()
        cap = []
        for i in words:
            a = list(i)
            a[2::3] = [x.upper() for x in a[2::3]]
            i = ''.join(a)
            cap.append(i)
        self.printdata(str(cap))
        output=self.writedata(str(cap))

    #Capitalize 5th word
    def Caps5(self):
        words =  self.readdata()
        for line in words:
            string = re.sub("[^a-zA-Z0-9]", " ", line).split(" ")
            for i in range(4, len(string), 5):
                string[i] = string[i].upper()
            self.printdata(str(string))
            output=self.writedata(str(string))

    #maxi function to check maximum element
    def maxi(self):
        count = 0
        word = ""
        maxCount = 0
        words = []
        file =  self.readdata()
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
        self.printdata(str(word))
        output=self.writedata(str(word))
    #opening file
    #To prefix method
    def ToPrefix(self):
        count1 = 0
        to = []
        file= self.readdata()
        for line in file:
            arr=line.split()
            for i in arr:
                if i.startswith("To"):
                    count1+=1
        to.append(count1)
        self.printdata(str(to))
        output=self.writedata(str(to))

    #ing suffix method
    def IngSuffix(self):
        file= self.readdata()
        count2=0
        ing=[]
        for line in file:
            arr=line.split()
            for i in arr:
                if i.endswith("ing"):
                    count2+=1
        ing.append(count2)
        self.printdata(str(ing))
        output=self.writedata(str(ing))

    #palindrome check
        # reverse function to check palindrome
    def reverse(self,s):
        str = ""
        for i in s:
            str = i + str
        return str

    def palindromeFunc(self):
        file= self.readdata()
        palindrome=[]
        for line in file:
            arr=line.split()
            for i in arr:
                if self.reverse(i)==i:
                    palindrome.append(i)
        output=self.writedata(str(palindrome))
        self.printdata(str(palindrome))

    #Adding words to a unique list
    def uniqueList(self):
        file= self.readdata()
        result=[]
        for line in file:
            arr=line.split()
            for i in arr:
                result.append(i)
        self.printdata(result)
        self.printdata(str(list(enumerate(result))))
        output1=self.writedata(str(result))
        output2=self.writedata(str(list(enumerate(result))))

option=int(input("Enter the option to display:"))
obj=Child()
if option==1:
    obj.ToPrefix()
elif option==2:
    obj.IngSuffix()
elif option==3:
    obj.palindromeFunc()
elif option==4:
    obj.uniqueList()
elif option==5:
    obj.maxi()
elif option==6:
    obj.Caps5()
elif option==7:
    obj.caps3()
elif option==8:
    obj.vowels()
elif option==9:
    obj.hyphen()
