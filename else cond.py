# 1st take a length and breadth from user and check its square or rectangle

l=int(input("enter a length"))
b=int(input("enter a breadth"))
if l==b:
    print("it's square")
else:
    print("it's reactangle")


print(" #########################################################################################################")

# 2nd write code inside function

def shape(l,b):
    if l==b:
        return "it is square"
    else:
        return "it's reactangle"
res=shape(int(input("enter a length")),int(input("enter a breadth")))
print(res)

print("****************************************************************************************************")

#3rd write a program to check its even or not

x=int(input("enter a number"))
if x%2==0:
    print("it's even")
else:
    print("it's not even")


print("**********************************************************************************************")

# 4th take string from user check its palindrome or not

s=input("enter a string")
if s==s[::-1]:
    print("palindrome")
else:
    print("not palindrome")

print("#####################################################################################################")

# 5th check its odd or not

x=int(input("enter a number"))
if x%2!=0:
    print("it's odd")
else:
    print("it's not odd")

print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$444444")

#6th read a number from user if number is divisible by either 2 or 6 then print hello python otherwise print hello django

n=int(input("enter a number"))
if n%2==0 or n%6==0:
    print("hello python")
else:
    print("hello django")

print("***********************************************************************************************************")

# 7th read anumber from user if it is divisible by both 3 and 9 then print hello world otherwise print hello india

n=int(input("enter a number"))
if n%3==0 and n%9==0:
    print("hello world")
else:
    print("hello india")

