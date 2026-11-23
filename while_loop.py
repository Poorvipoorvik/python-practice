# simple while example to print number
a=1
while a<=11:
    print(a)
    a=a+1

print("__________________________________________________________________________________________________________-")

# print 7 th tables using while loop
a=1
while a<=10:
    print("7*",a,"=",7*a)
    a=a+1

print("__________________________________________________________________________________________________________________")

# print all lower case alphabets using while loop
a=97
while a<=122:
    print(chr(a), end=" ")
    a=a+1

print("---------------------------------------------------------------------------------------------------")
# print all lower case alphabets in reverse order

a=122
while a>=97:
    print(chr(a), end=" ")
    a= a-1

print("___________________________________________________________________________________________")

# print all upper case alphabets using while loop 
a=65
while a<=90:
    print(chr(a), end=" ")
    a=a+1



print("----------------------------------------------------------------------------------------------------")

# print all upper case alphabets in reverse order using in while loop

a=90
while a>=65:
    print(chr(a), end = " ")
    a=a-1


print("-------------------------------------------------------------------------------------------------------------")


# print the reverse order of 5th table

a=10
while a>=1:
    print("5*",a,"=",a*5)
    a=a-1