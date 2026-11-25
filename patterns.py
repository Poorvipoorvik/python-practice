#%%
# square patters
n=int(input("enter a number"))
for i in range(n):
    for j in range(n):
        print("#",end=" ")
    print()
#%%
# right angle triangle
n=int(input("enter a number"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("$",end=" ")
    print()
#%%
# reverse angle triangle
n=int(input("enter a number"))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print("@",end=" ")
    print()
#%%
# left angle triangle
n=int(input("enter a number"))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(1,i+1):
        print("%",end=" ")
    print()
#%%
# inverted left angle triangle
n=int(input("enter a number"))
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(1,i+1):
        print("%",end=" ")
    print()
#%%
n=int(input("enter a number"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(96+j),end=" ")
    print()
#%%
n=int(input('enter a number'))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(n,end=" ")
        n+=1
    print()
#%%
#pyramid 
n=int(input('enter a number'))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("%",end=" ")
    print()
#%%
# inverted pyramid
n=int(input('enter a number'))
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("%",end=" ")
    print()
#%%
# 
n=97
for i in range(1,5):
    for j in range(1,i+1):
        print(chr(n),end=" ")
        n+=1
    print()
#%%
