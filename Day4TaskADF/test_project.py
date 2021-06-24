import pytest
import re
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
        with open('filenew. txt', 'w+') as f:
            for i in data:
                f.write("%s"%i)
            print("Text written into the file. Check it!!")
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
        # self.printdata(str(res))
        output=res
        return output

    def hyphen(self):
        list =  self.readdata()
        list1=[]
        for line in list:
            string=line.replace(" ","-")
            list1.append(string)
        # self.printdata(str(list1))
        output=list1
        return output
        # print(output)

    def semi(self):
        list =  self.readdata1()
        res = list.replace("\n",";")
        # self.printdata(str(res))
        output=res
        # print(output)
        return output

    def caps3(self):
        words = self.readdata()
        cap = []
        for i in words:
            a = list(i)
            a[2::3] = [x.upper() for x in a[2::3]]
            i = ''.join(a)
            cap.append(i)
        # self.printdata(str(cap))
        output = cap
        # print(output)
        return output

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
        # self.printdata(str(word))
        output=word
        # print(output)
        return output

    def Caps5(self):
        words =  self.readdata()
        for line in words:
            string = re.sub("[^a-zA-Z0-9]", " ", line).split(" ")
            for i in range(4, len(string), 5):
                string[i] = string[i].upper()
            # self.printdata(str(string))
            output=string
            # print(output)
            return output

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
        # self.printdata(str(to))
        output=to
        # print(output)
        return output

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
        # self.printdata(str(ing))
        output=ing
        return output

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
        output=palindrome
        # self.printdata(str(palindrome))
        return output

    def uniqueList(self):
        file= self.readdata()
        result=[]
        for line in file:
            arr=line.split()
            for i in arr:
                result.append(i)
        # self.printdata(result)
        # self.printdata(str(list(enumerate(result))))
        output1=result
        return output1
        # output2=str(list(enumerate(result)))

    def keyvalue(self):
        file = self.readdata()
        result = []
        for line in file:
            arr = line.split()
            for i in arr:
                result.append(i)
        output=list(enumerate(result))
        return output
        # print(output)

class TestClass(Child):
    def test_method(self):
        l=[]
        l=self.vowels()
        assert l[0]=='T g th r'
    def test_method1(self):
        l=[]
        l=self.hyphen()
        assert l[1]=='TooT-riding\n'
    def test_method2(self):
        l=[]
        l=self.semi()
        assert l=='Together we gonna go riding and writing;TooT riding;'
    def test_method3(self):
        l=[]
        l=self.caps3()
        assert l[1]=='ToOT RidIng\n'
    def test_method4(self):
        l=self.maxi()
        assert l=='riding'
    def test_method5(self):
        l=[]
        l=self.Caps5()
        assert l==['Together', 'we', 'gonna', 'go', 'RIDING', 'and', 'writing', '']
    def test_method6(self):
        l=[]
        l=self.ToPrefix()
        assert l==[2]
    def test_method7(self):
        l=[]
        l=self.IngSuffix()
        assert l==[3]
    def test_method8(self):
        l=[]
        l=self.palindromeFunc()
        assert l==['TooT']
    def test_method9(self):
        l = []
        l = self.uniqueList()
        assert l == ['Together', 'we', 'gonna', 'go', 'riding', 'and', 'writing', 'TooT', 'riding']
    def test_method10(self):
        l=[]
        l=self.keyvalue()
        assert l == [(0, 'Together'), (1, 'we'), (2, 'gonna'), (3, 'go'), (4, 'riding'), (5, 'and'), (6, 'writing'), (7, 'TooT'), (8, 'riding')]

obj=Child()
obj.vowels()
obj.hyphen()
obj.semi()
obj.caps3()
obj.maxi()
obj.Caps5()
obj.ToPrefix()
obj.IngSuffix()
obj.palindromeFunc()
obj.uniqueList()
obj.keyvalue()