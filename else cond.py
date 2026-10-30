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