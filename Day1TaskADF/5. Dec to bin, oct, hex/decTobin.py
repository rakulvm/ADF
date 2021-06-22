num=int(input("Enter the number:"))
binary=""
while num!=0:
    reminder=num%2
    num//=2
    binary=str(reminder)+binary
print("Decimal to binary is",binary)
#printing using built-in
print("Binary using bin function is:",bin(num))
#finding using function call
def findBin(n):
    if n>1:
        findBin(n//2)
    print(n%2, end="")
dec=int(input("Enter the number"))
print("Decimal to binary using recursion is: ")
findBin(dec)
