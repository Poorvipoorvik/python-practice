#%%
# move 0s and 1s to order
l=[0,1,0,1,1,0,0,1,1,1,1,0,0,0,0]
zeros=[]
ones=[]
for i in l:
    if i == 0:
        zeros+=[i]
    else:
        ones+=[i]
print(zeros+ones)
#%%
# palindrome or not

n=input("enter a value")
n1=" "
for i in range(len(n)-1,-1,-1):
    n1 += n[i]
if n==n1:
    print("palindrome")
else:
    print("not palindrome")
#%%
# palindrome or not
n="101"
n1=" "
if n==n[::-1]:
    print("palindrome")
else:
    print("not palindrome")
#%%
# prime or not

a=int(input("enter a number"))
c=0
for i in range(2,a):
    if a%i==0:
        c+=1
if a>1 and c==0:
    print("even")
else:
    print("not even")
#%%
# armstrong number

n=int(input("enter a number"))
sum=0
pow=len(str(n))
temp=n

while temp>0:
    digit=temp%10
    sum=sum+digit ** pow
    temp=temp//10
if sum==n:
    print("armstron number")
else:
    print("not armstron")
#%%
# to find biggest number in list
l=[12,34,32,56,87,98,9,89]
big=l[0]
for i in range(len(l)):
    if l[i]>big:
        big=l[i]
print(big)
#%%
# character count
n=input("enter a string")

d={}
for i in n:
    if i not in d:
        d[i]=1
    else:
        d[i]=d[i]+1
print(d)
#%%
#second biggest
l=[12,34,32,56,87,98,9,89]
big=l[0]
second=l[0]
for i in range(len(l)):
    if l[i]>big:
        second=big
        big=l[i]
    elif l[i]>second and l[i]!=big:
        second=l[i]
print(second)

#%% md

#%%
