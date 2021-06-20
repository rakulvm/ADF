                                                          ADF Python Day - 1
1. Read a file and write only unique words in another file :-**
   - I intially declared a set. Then I read file "rakul.txt" and stored it in variable "f".
   - Then I iterated every line and split and changed every special characters as space by using regex for each word.
   - Simulataneously, I found the length of each word and concatenated both length and string. 
   - And finally I've added that in the set which I've declared before. 
   - I've used set to remove all duplicates and took unique words. 
   - Then I've typecasted the set back to list and perform sort function based on length of the string.******

2. Read CSV file and store it in Python Dictionary :-
   - I've created a CSV file in my PC and imported CSV in my python file. 
   - I've Read that file using python file reading and stored it in a variable named reader.
   - Here I created one dictionary called "people" which constists of name, age, and department. 
   - After that I've iterated every row in that CSV file.
   - In that ditionary 0th value taken as key and remaining stored with the base of that particular key in dictionary.

3. Display all prime numbers with the interval of 5 seconds :-
   - At first, I imported time. Here I created an integer i which is iterating variable upto infinity through while loop.
   - In every iteration, I checked that number is prime or not.
   - If I get prime number, then display it and put the program to sleep for 5 seconds using "time.sleep(5)".
   - If it is not prime number number, then proceed for the further iteration.

4. GCD / HCF of 2 numbers :-
   - Initially get 2 numbers as input from the user.
   - I re-initialised those 2 variables as absolute values so that negative values can also be calculated.
   - I found smallest of that 2 numbers.
   - If those 2 are 0, I'll print"Can't find GCD".
   - At that same time I checked the condition (a%i==0 && b%i==0) in every iteration.
   - If this condition satisfies, then it that particular "i" is the GCD of that 2 numbers.
   - Finally I'll print the gcd in print statement.

5. Decimal to Binary, Octal, Hexadecimal :-
   - At first, I'll get one decimal value as input from the user.
   - And after that I used inbuilt python functions like bin(), oct(), hex() to get binary, octal, hexadecimal value for that input respectively. 
   - Finally display it everything.

6. Ascii value for given character :-
   - Intially I get one character value as input from the user.
   - And after that I used inbuilt python function ord() to get ascii value for the input.
   - Finally I displayed that ascii value.

7. User Application (name, age, gender, salary, state, city) :-
   - Get string as input for name, age, gender, state, city, and also get one float value for salary from the user. 
   - Finally I display it everything to the user.
