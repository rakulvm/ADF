num=int(input("Enter the number:"))
octal=""
while num!=0:
    rem=num%8
    num//=8
    octal=str(rem)+octal
print("\nThe Decimal to Octal value:",octal)
#printing using built-in function
print("The Decimal to Octal value using bin function is:",oct(num))
#printing using recursion
def octal(n):
    if n>1:
        octal(int(n/8))
    print(n%8, end="")
dec=int(input("Enter the Decimal value:"))
octal(dec)