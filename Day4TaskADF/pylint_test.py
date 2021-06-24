"""method"""
import re
import logging
logging.basicConfig(
    filename="test.log",
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s")
class Parent():
    """method"""
    # File_new= ""
    # def init(self,FILE_NEW):
    #     """method"""
    #     self.FILE_NEW=FILE_NEW

    @classmethod
    def readdata1(cls):
        """method"""
        with open("rakul.txt", 'r') as file1:
            lines= file1.read()
        file1.close()
        return lines

    @classmethod
    def readdata(cls):
        """method"""
        with open("rakul.txt", 'r') as file2:
            lines = file2.readlines()
        file2.close()
        return lines

    @classmethod
    def writedata(cls, data):
        """method"""
        with open('filenew.txt', 'w+') as file1:
            for i in data:
                file1.write("%s"%i)
        print("Text written into the file. Check it!!")
        logging.debug("Starting with to")
        file1.close()

class Child(Parent):
    """common method for printing the results"""
    @classmethod
    def printdata(cls,data):
        """method"""
        print(data)
    def vowels_func(self):
        """Split the words based on the vowels"""
        lista = self.readdata()
        list1=[]
        for line in lista:
            string = re.sub("[^0-9a-zA-Z]", " ",line).split(" ")
            for word in string:
                if word!="":
                    list1.append(word)
        res=[re.sub("[aeiouAEIOU]",' ',i) for i in list1]
        # self.printdata(str(res))
        output=res
        return output
    def hy_phen(self):
        """method"""
        lista =  self.readdata()
        list1=[]
        for line in lista:
            string=line.replace(" ","-")
            list1.append(string)
        # self.printdata(str(list1))
        output=list1
        return output
        # print(output)
    def semi_colon(self):
        """method"""
        lista =  self.readdata1()
        res = lista.replace("\n",";")
        # self.printdata(str(res))
        output=res
        # print(output)
        return output
    def caps_3(self):
        """method"""
        words = self.readdata()
        cap = []
        for i in words:
            appen = list(i)
            appen[2::3] = [x.upper() for x in appen[2::3]]
            i = ''.join(appen)
            cap.append(i)
        # self.printdata(str(cap))
        output = cap
        # print(output)
        return output
    def max_i(self):
        """method"""
        count = 0
        word = ""
        maxcount = 0
        words = []
        file =  self.readdata()
        for line in file:
            # string = line.lower().replace(',', '').replace('.', '').split(" ")
            string = re.sub("[^A-Za-z0-9]"," ",line).split(" ")
            for stri in string:
                words.append(stri)
        len_word=len(words)
        for i in range(0, len_word):
            count = 1
            for j in range(i + 1, len(words)):
                if words[i] == words[j]:
                    count = count + 1
                # count=count+1 if words[i]==words[j] else continue
            if count > maxcount:
                maxcount = count
                word = words[i]
        # self.printdata(str(word))
        output=word
        # print(output)
        return output
    def caps_5(self):
        """method"""
        words =  self.readdata()
        for line in words:
            string = re.sub("[^a-zA-Z0-9]", " ", line).split(" ")
            for i in range(4, len(string), 5):
                string[i] = string[i].upper()
            # self.printdata(str(string))
            output=string
            # print(output)
            return output
    def to_prefix(self):
        """method"""
        count1 = 0
        to_list = []
        file1= self.readdata()
        for line in file1:
            arr=line.split()
            for i in arr:
                if i.startswith("To"):
                    count1+=1
        to_list.append(count1)
        # self.printdata(str(to))
        output=to_list
        # print(output)
        return output
    def ing_suffix(self):
        """method"""
        file1= self.readdata()
        count2=0
        ing=[]
        for line in file1:
            arr=line.split()
            for i in arr:
                if i.endswith("ing"):
                    count2+=1
        ing.append(count2)
        output=ing
        return output
    @classmethod
    def reverse(cls,sel):
        """method"""
        str1 = ""
        for i in sel:
            str1 = i + str1
        return str1
    def palindrome_func(self):
        """method"""
        file1= self.readdata()
        palindrome=[]
        for line in file1:
            arr=line.split()
            for i in arr:
                if self.reverse(i)==i:
                    palindrome.append(i)
        output=palindrome
        # self.printdata(str(palindrome))
        return output
    def unique_list(self):
        """method"""
        file1= self.readdata()
        result=[]
        for line in file1:
            arr=line.split()
            for i in arr:
                result.append(i)
        # self.printdata(result)
        # self.printdata(str(list(enumerate(result))))
        output1=result
        return output1
        # output2=str(list(enumerate(result)))
    def key_value(self):
        """method"""
        file1 = self.readdata()
        result = []
        for line in file1:
            arr = line.split()
            for i in arr:
                result.append(i)
        output=list(enumerate(result))
        return output
        # print(output)
# class TestClass(Child):
#     """method"""
#     def test_method(self):
#         """method"""
#         assert self.vowels_func()[0]=='T g th r'
#     def test_method1(self):
#         """method"""
#         assert self.hy_phen()[1]=='TooT-riding\n'
#     def test_method2(self):
#         """method"""
#         assert self.semi_colon()=='Together we gonna go riding and writing;TooT riding;'
#     def test_method3(self):
#         """method"""
#         assert self.caps_3()[1]=='ToOT RidIng\n'
#     def test_method4(self):
#         """method"""
#         assert self.max_i()=='riding'
#     def test_method5(self):
#         """method"""
#         assert self.caps_5()==['Together', 'we', 'gonna', 'go', 'RIDING', 'and', 'writing', '']
#     def test_method6(self):
#         """method"""
#         assert self.to_prefix()==[2]
#     def test_method7(self):
#         """method"""
#         assert self.ing_suffix()==[3]
#     def test_method8(self):
#         """method"""
#         assert self.palindrome_func()==['TooT']
#     def test_method9(self):
#         """method"""
#         assert self.unique_list()== ['Together', 'we', 'gonna', 'go',
#                        'riding', 'and', 'writing', 'TooT', 'riding']
#     def test_method10(self):
#         """method"""
#         assert self.key_value()== [(0, 'Together'), (1, 'we'), (2, 'gonna'), (3, 'go'),
#                        (4, 'riding'), (5, 'and'), (6, 'writing'), (7, 'TooT'), (8, 'riding')]
obj=Child()
obj.vowels_func()
obj.hy_phen()
obj.semi_colon()
obj.caps_3()
obj.max_i()
obj.caps_5()
obj.to_prefix()
obj.ing_suffix()
obj.palindrome_func()
obj.unique_list()
obj.key_value()
