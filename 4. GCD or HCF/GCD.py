#Find GCD of a number
a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
a=abs(a)
b=abs(b)
smaller=0
gcd=0

if a==0 or b==0:
   print("Can't find GCD")
   exit()

if a<b:
    smaller=a
elif a==b or b<a:
    smaller=b

if a<0 and b>0:
    gcd=b
elif b<0 and a>0:
    gcd=a
else:
    for i in range(1,smaller+1):
        if ((a%i==0) and (b%i==0)):
            gcd=i

print(gcd)


