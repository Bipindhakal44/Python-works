#to find the area of a circle
r=float(input("Enter the radius of the circle "))
a=3.14*r*r
print("The area of the circle is",a)

#to find the area of a rectangle
l=float(input("Enter the length of the rectangle "))
b=float(input("Enter the breadth of the rectangle "))
a=l*b
print("The area of the rectangle is",a,"cm2")

#to print the area of a triangle
a=float(input("Enter the length of the 1st side of the triangle "))
b=float(input("Enter the length of the second side of the triangle "))
c=float(input("Enter the length of the third side of the triangle "))
s=a+b+c
t=s*(s+a)*(s+b)*(s+c)
print("The area of the triangle is",t,"cm2")

#to print the SI
p=float(input("Enter the principal value "))
t=float(input("Enter the time duration "))
r=float(input("Enter the rate of the interest "))
si=(p*t*r)/100
print("The Simple Interest is",si,"% per annum")

#To print the Grand total marks, percentage and the grade
a=int(input("Enter the marks in english: "))
b=int(input("Enter the marks in maths: "))
c=int(input("Enter the marks in chemistry: "))
d=int(input("Enter the marks in physics: "))
if a<40 or b<40 or c<40 or d<40:
    print("Fail")
else:
    e=a+b+c+d
    if e>400:
        print("Error")
    else:
        print("The Grand Total marks is: ", e)
    f = (e / 400) * 100
    if f > 100:
        print("Error")
    else:
        print("The percentage you secured is: ", f, "%")
    if f >= 70:
        print("Distinction")
    elif f >= 60:
        print("First Division")
    elif f >= 40:
        print("Pass")
    else:
        print("Fail")

#To print seconds into days, hours,  minutes and seconds
sec=int(input("Enter the time in seconds: "))
a=sec%86400
b=a%3600
c=b%60
if sec>=86400:
    print('The time is:',sec//86400,'days',a//3600,'Hours',b//60,'Minutes',c,'Seconds')
elif sec<86400:
    print('The time is', a // 3600, 'Hours', b // 60, 'Minutes', c, 'Seconds')

#To print whether the user input number is even or odd
a=int(input("Enter any number: "))
if a<0:
    print("The given number is a negative number")
elif a==0:
    print("Zero")
elif a%2==0:
    print("The given number is an even number")
elif a%2==1:
    print("The given number is an odd number")

#To print whether the user input number is positive, negative or zero
a=int(input("Enter any number: "))
if a==0:
    print("Zero")
elif a<0:
    print("False")
elif a>0:
    print("True")

#To print the last digit of an integer number
a=input("Enter any number: ")
print(a[-1])

#To find the sum of the individual digits of a three digit number
a=input("Enter any three digit number: ")
b=int(a[0])
c=int(a[1])
d=int(a[2])
sum=b+c+d
print("The sum of the individual digits of the three digit number is: ",sum)

list=(1,2,3,4,5)
b=5
print(b in list)

#To print the amount of yearly tax
tax=int(input("Enter the amount of yearly earning: "))
if tax<=400000:
    a=tax*0.01
    print("Your yeraly tax amount is: ",a)
elif tax>400000 and tax<=600000:
    e=tax-600000
    b=(400000*0.01)+((tax-400000-int(e))*0.05)
    print("Your yearly tax amount is: ",b)
elif tax>600000 and tax<=900000:
    c=(400000*0.01)+((tax-400000)*0.05)+((tax-600000)*0.15)
    print("Your tax amount is: ",c)
elif tax>900000:
    d=(400000*0.01)+((tax-400000)*0.05)+((tax-600000)*0.15)+((tax-900000)*0.25)
    print("Your tax amount is: ",d)

#WAP to built an arithmetic calculator
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def mul(a,b):
    print(a*b)
def div(a,b):
    print(a/b)
c=int(input('''1. Enter 1 for addition
2. Enter 2 for subtraction
3. Enter 3 for multiplication
4. Enter 4 for division: '''))
if c<1:
    print("Error input")
if c>4:
    print("Error input")
if c==1:
    add(a,b)
elif c==2:
    sub(a,b)
elif c==3:
    mul(a,b)
elif c==4:
    div(a,b)

#To print the largest number amongst three given numbers
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
if a>b and a>c:
    print("The largest number is ",a)
elif b>a and b>c:
    print("The largest number is ",b)
elif c>a and c>b:
    print('The largest number is ',c)

#WAP to find the sum of first 50 natural numbers
a=1
b=0
while a<=50:
    b=b+a
    a=a+1
print(b)

# WAP to take an user input and find if the user given number is prime or not
a = int(input("Enter any number: "))
b = 1
c=0
while b <= a:
    if a % b == 0:
        c=c+1
    b=b+1
if c==2:
    print("Prime Number")
elif c>2:
    print("Composite Number")

# WAP to find all the odd and even number between 50 to 100 using while loop
a=50
while a <= 100:
    if a % 2 == 1:
        print(a)
    a = a + 1

#WAP to check whether an user input number is palindrome or not
a=int(input("Enter any number: "))
c=0
x=a
while a>0:
    b=a%10
    c=c*10+b
    a=a//10
if x==c:
    print("The Number is Palindrome")
else:
    print("The Number is not Palindrome")

#WAP to check whether an user input number is an armstrong number or not
a=int(input("Enter any number: "))
b=0
d=a
e=len(str(a))
while a>0:
    c=a%10
    b=b+c**e
    a=a//10
if b==d:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
print(b)

#for <i> in range([start],stop,[step]]):
#   statement

for i in range(1,10,1):
    print("Nitesh")
for i in range(8):
    print("bhatta")
for i in range(2,11,2):
    print(i)
for i in range(1,11,2):
    print(i)

#Sum
a=0
for i in range(1,11,1):
    a=a+i
print(a)

#Factorial
fact=1
for i in range(2,6):
    fact=fact*i
print(fact)

#Sequence in strings
name="nitesh bhatta"
for i in name:
    print(i)

#For and else
for i in range(4):
    print(i)
else:
    print("over")

#Break Statement

#break changes the control flow from loop to out of the loop
for i in range(4):
    if i==2:
        break
    print(i)
else:
    print("Over")
#continue skips the equivalent value and continues the execution of the loop and then goes to out of the loop
for i in  range(4):
    if i==2:
        continue
    print(i)
else:
    print("Over")

#car game
command=""
while True:
    user_command=input("> ").lower()
    if user_command=="help":
        print('''> start - to start the car
> stop - to stop the car
> quit - to exit''')
    elif user_command=="start":
        print("> Car started")
    elif user_command=="stop":
        print("> Car stopped")
    elif user_command=="quit":
        break
    else:
        print("I don't understand that!")

#WAP to find the sum of a digits of given  number input  by an user
number=input("Enter input any number: ")
length=len(number)
a=0
b=0
while a<length:
    b=b+int(number[a])
    a=a+1
print(b)

#Easy way to print the sum of individual digits of any number
number=int(input("Enter any number: "))
a=0
while number>0:
    b=number%10
    a=a+b
    number=number//10
print(a)

#To print the sum of individual digits of a number using for loop
number=input("Enter any number: ")
length=len(str(number))
sum=0
for i in range(0,length,1):
    sum=sum+int(number[i])
print(sum)

#WAP to print the factorial of any number
number=int(input("Enter any number: "))
fact=1
while number>0:
    fact=fact*number
    number=number-1
print(fact)

#To print the factorial of any number using for loop
number=int(input("Enter any number: "))
fact=1
for i in range(0,number,1):
    fact=fact*number
    number=number-1
print(fact)

#To print the factorial of an number using function
def factorial(num):
    fact=1
    while num>0:
        fact=fact*num
        num=num-1
    print(fact)

factorial(4)

#To print the sum of the individual digits using functions
def sum(num):
    a=0
    while num>0:
        b=num%10
        a=a+b
        num=num//10
    print("The sum of the individual digits of the given number is ",a)

sum(123)

def factorial(num):
    if num==1:
        return 1
    else:
        return num*(factorial(num-1))

#factorial of a number using recursion
def factor(num):
    if num==1:
        return 1
    else:
        return (num*(factor(num-1)))

num=int(input("Enter any number: "))
fact=factor(num)
print("The factorial is ",fact)

#WAP to print out first 20 fibonacci series starting from 1 using while loop
first_num=1
second_num=1
counter=1
while counter<=20:
    print(first_num,end=" ")
    third_num=first_num+second_num
    first_num=second_num
    second_num=third_num
    counter=counter+1

#WAP to print out first 20 fibonacci series starting from 1 using for loop
first_num1=1
second_num1=1
for i in range(0,20,1):
    print(first_num,end=" ")
    third_num1=first_num1+second_num1
    first_num1=second_num1
    second_num1=third_num1

#To print the numbers between 2000 and 3000 which are perfectly divisible by 7 and not a multiple of 5
first_num=2000
while first_num<=3000:
    mod=first_num%7
    mod1=first_num%5
    if mod==0 and mod1!=0:
        print(first_num,end=" ")
    first_num=first_num+

#To print the stars upto a user given limit
a=int(input("Enter any number: "))
b=1
while b<=a:
    print(b*"*")
    b=b+1

#LIST
num=[2,4,6,8,10]
print(num)

#num.append to insert a value at the last of the list
#num.insert(index,value) to insert a value at a specific position in a list

#To take five numbers as input to form a list and print the list as well as the sum of the numbers in the list
num=[]
a=int(input("Enter any numbers: "))
b=int(input("Enter any numbers: "))
c=int(input("Enter any numbers: "))
d=int(input("Enter any numbers: "))
e=int(input("Enter any numbers: "))
num.insert(0,a)
num.insert(1,b)
num.insert(2,c)
num.insert(3,d)
num.insert(4,e)
print(num)
counter=0
sum=0
while counter<=4:
    numb=int(num[counter])
    sum=sum+numb
    counter=counter+1
print(sum)

#To take 10 numbers as input and print the list as well as the largest among them, smallest among them and a list of odd numbers among them
#To take 10 numbers as input from the user and make a list of numbers in ascending order
odd=[]
ascend=[]
for i in range(0,10):
    num=int(input("Enter a number: "))
    ascend.insert(i,num)
counter=0
while counter<=9:
    numb=int(num[counter])
    mod=numb%2
    if mod==1:
        odd.insert(counter,numb)
    counter=counter+1
print(odd)

#To print a list of numbers in reverse order
num = [1, 2, 3]
rev=[]
counter = -1
pin = 0
while counter > -4:
    numb = int(num[counter])
    rev.insert(pin, numb)
    counter = counter - 1
    pin = pin + 1
print(rev)

#To take 10 numbers as input from the user and make a list of numbers in ascending order
ascend=[]
ascend1=[]
for i in range(0,10):
    num=int(input("Enter a number: "))
    ascend.insert(i,num)
counter=0
while counter<=9:
    num=min(ascend)
    ascend1.insert(counter,num)
    ascend.remove(num)
    counter=counter+1
print(ascend1)

#To take 10 numbers as input from the user and make a list of numbers in ascending order
num=[5,4,3,2,1]
i=0
while i<5:
    j=0
    while j<4:
        if num[j]>num[j+1]:
            temp=num[j]
            num[j]=num[j+1]
            num[j+1]=temp
        j=j+1
    i=i+1
print(num)

#WAP to take an user input a word and find out if the user given word is palindrom or not
word=input("Enter any word: ")
length=-(len(word))
string1=""
counter=-1
while counter>(length-1):
    string=word[counter]
    string1=string1+string
    counter=counter-1
if string1==word:
    print("The user input string is a palindrome")
else:
    print("The user input string is not palindrome")

#To print stars in reverse order
a=5
b="*"
while a>=0:
    print(a*b)
    a=a-1

# WAP to take an user input of list of 10 numbers and print how many times a specific number is repeated
# WAP to take an input of list of 10 numbers and sort the list and find the following
# mean
# median
# mode
repeat = []
repeat1=[]
for i in range(0, 10):
    num = int(input("Enter any number: "))
    repeat.insert(i, num)
print(repeat)
counter = 0
while counter <= 9:
    num = 0
    while num<=8:
        if repeat[num] == repeat[num + 1]:
            store = repeat[num]
            repeat1.insert(num,store)
            repeat[num]=repeat[num+1]
            num=num+1
    counter=counter+1
print(repeat1)

#WAP to print the numbes between 1500 and 2700 which are divisible bt 5 and 7 and are multiples of 5
counter=1500
print("The numbers divisible by 5 and 7 and multiples of 5 are: ")
while counter<=2700:
    seven=counter%7
    five=counter%5
    if seven==0 and five==0:
        print(counter,end=" ")
    counter=counter+1

#WAP to guess a number between 1 to 9
right_num=4
counter=1
while counter<=9:
    guess=int(input("Guess a number: "))
    if right_num==guess:
        print("Well Guessed!")
        break
    elif guess!=right_num:
        counter=counter+1

#SnowFlake Turtle
import turtle
import random

# setup the window with a background colour
wn = turtle.Screen()
wn.bgcolor("#EFECCA")
wn.setup(width=250, height=250)

# assign a name to your turtle
turtle = turtle.Turtle()
turtle.speed(100)

colors = ["#7D8A2E", "#263248", "#FF8C00", "#F0C600"]

#
def snowflake(size, pensize, x, y):
    """ function that draws a snowflake """
    # turtle.pen(pensize=10)
    turtle.penup()
    turtle.goto(x, y)
    turtle.forward(10*size)
    turtle.left(45)
    turtle.pendown()
    turtle.color(random.choice(colors))

    for i in range(8):
        branch(size)
        turtle.left(45)


# create one branch of the snowflake
def branch(size):
    for i in range(3):
        for i in range(3):
            turtle.forward(10.0*size/3)
            turtle.backward(10.0*size/3)
            turtle.right(45)
        turtle.left(90)
        turtle.backward(10.0*size/3)
        turtle.left(45)
    turtle.right(90)
    turtle.forward(10.0*size)

snowflake(8, 6, 0, 0)

# leave the window open until you click to close
wn.exitonclick()

#Mandaa Art
import turtle
wn=turtle.Screen()
pen=turtle.Turtle()

pen.speed(100)
pen.pendown()
for i in range(75):
    pen.forward(10)
    pen.left(65)
    pen.forward(10)
    pen.right(135)
    pen.forward(10)
    pen.left(65)
    pen.forward(10)
    pen.left(65)
    pen.forward(10)
    pen.left(65)
    pen.forward(10)
    pen.right(135)
    pen.forward(10)
    pen.left(65)
    pen.forward(10)
    pen.right(135)
    pen.forward(10)
    pen.left(65)
    pen.forward(10)
    pen.right(135)
    pen.forward(10)
    pen.left(65)
    pen.forward(10)
    pen.left(65)
    pen.forward(10)
    pen.left(65)
    pen.forward(10)
    pen.right(135)
    pen.forward(10)
    pen.left(65)
    pen.forward(10)
turtle.done()


#Turtle Dragging
import turtle
from turtle import Screen, Turtle

screen = Screen()
t = Turtle("turtle")
t.speed(-1)


def dragging(x, y):  # These parameters will be the mouse position
    t.ondrag(None)
    t.setheading(t.towards(x, y))
    t.goto(x, y)
    t.ondrag(dragging)


def clickRight():
    t.clear()
