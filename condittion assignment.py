# 1st read number from keybord 
# a) if is divisible by 3 print Fizz
# b) if is divisible by 5 print Buzz
# c) if is divisible by both 3 and 5 print FizzBuzz
# d) not divisible any number print fizzbuzz

n=int(input("enter a number :"))
if n% 3==0 and n%5==0:
    print("FizzBuzz")
elif n%3==0:
    print("Fizz")
elif n%5==0:
    print("Buzz")
else:
    print("buzzfizz")

print("#################################################################################################################")

# 2nd read a number from keybord
# a) if number between 1 to 100 print good morning
# b) if number between 100 to 500 print good afternoon
# c) if number between 500 to 100 print good evening 
# other than any number then print good night

n=int(input("enter a number :"))
if n>=1 and n<100:
    print("Good Morning")
elif n>=100 and n<500:
    print("Good Afternoon")
elif n>=500 and n<100:
    print("Good Evening")
else:
    print("Good Night")

print("#####################################################################################################################")

# 3 rd find biggest of 3 number

a=int(input('enter a number1:'))
b=int(input('enter a number2:'))
c=int(input('enter a number3:'))
if a>b and a>c:
    print(a,": biggest number1")
elif b>a and b>c:
    print(b,": biggest number2")
else:
    print(c,": biggest number3")

#4th read age and name from user if age graterthan equal to 18 print name and eligible for voting otherwise print name and not eligible for voting

name=input("enter a name :")
age=int(input("enter a age :"))
if age >=18:
    print(name," is eligible for voting")
else:
    print(name," is not eligible for voting")

#5 th check number is positive or negetive

n=int(input("enter a number :"))
if n>=0:
    print("positive number is :",n)
else:
    print("negative number is :",n)

# 6th check number is even or odd

n=int(input("enter a number :"))
if n%2==0:
    print("even number is :",n)
else:
    print("odd number is :",n)

# 7th take string from user check it is vowel or constant

s=input("enter a character:")
if s in "aeiouAEIOU":
    print("it's vowel")
else:
    print("it's constant")

print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

# 8th shop give 10 % discount if cost purchased more than 1000 ask user for quantity one quantity is 100 then judge and print if he no purchase more than 
# 1000 then keep the total cost as same 

q=int(input("enter a quantity :"))
total=q*100
if total >1000:
    discout=total*10/100
    total=total-discout
    print(total)
else:
    print(total)