import time
i=0
print("The prime values are:")
while True:
   a = False
   i+=1
   for j in range(2,i):
       if i%j==0:
          a=True
   if a==False:
       time.sleep(5)
       #prints every 5 seconds as mentioned in the question
       print(i,end=" ")