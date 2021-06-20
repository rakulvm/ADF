conversion_table = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
decimal = int(input("Enter a number: "))
hexadecimal = ""

while (decimal > 0):
    remainder = decimal % 16
    hexadecimal = conversion_table[remainder] + hexadecimal
    decimal = decimal // 16
print("Hexadecimal: ", hexadecimal)

#printing using built-in function
print("The Decimal to Octal value using bin function is:",hex(decimal))

#printing using recursion
def decTohex(n):
    if (n <= 0):
        return ''
    remainder = n % 16
    return decTohex(n // 16) + conversion_table[remainder]
decimal = int(input("Enter a number: "))
print("Hexadecimal value is: ", decTohex(decimal))