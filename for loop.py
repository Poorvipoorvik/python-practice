#%%
# ask user to enter a string and print vowels in  given string

a=input("enter a name")
for i in a:
    if i in ("aeiouAEIOU"):
        print(i)
#%%
# ask user to enter a string and print consonents in  given string

a=input("enter a name")
for i in a:
    if i.isalpha() and i not in ("aeiouAEIOU"):
        print(i)
#%%
# take a list with 10 elements and print all even number
l=[10,20,34,21,35,67,88,12,67,31]
for i in l:
    if i %2==0:
        print(i)
#%%
# take a tuple with 10 elements and print all odd number
l=(10,20,34,21,35,67,88,12,67,31)
for i in l:
    if i %2!=0:
        print(i)
#%%
# for loop example with loop
# access only key
d={
    "name":"raju",
    "age":35,
    "place":"BNG"
}
for i in d:
    print(i)

# access only value
for i in d.keys():
    print(i)

# access both keys and values
for i,j in d.items():
    print(i,":",j)
#%%
# take list with 5 elements and access even index elements

l=[10,20,32,1,2]
for i in range(0,len(l),2):
    print(l[i])
#%%
# take list with 5 elements and access odd index elements

l=[10,20,32,1,2]
for i in range(1,len(l),2):
    print(l[i])
#%%
# take list with 10  elements and access even index even  elements

l=[10,20,32,1,2,56,31,5,23,22]
for i in range(0,len(l),2):
    if l[i]%2==0:
        print(l[i])
#%%
# take list with 10  elements and access even index odd elements

l=[10,20,32,1,2,56,31,5,23,22]
for i in range(0,len(l),2):
    if l[i]%2!=0:
        print(l[i])
#%%
# take list with 10  elements and access odd index even elements

l=[10,20,32,1,2,56,31,5,23,22]
for i in range(1,len(l),2):
    if l[i]%2==0:
        print(l[i])
#%%
# take list with 10  elements and access odd index odd elements

l=[10,20,32,1,2,56,31,5,23,22]
for i in range(1,len(l),2):
    if l[i]%2!=0:
        print(l[i])
#%%
# read 5 elements from user and store in it list
l=[]
for i in range(5):
    a=int(input("enter a number"))
    l+=[a]
    print(l)
# access even index odd elements

for i in range (0,len(l),2):
    if l[i]%2!=0:
        print(l[i])
#%%
# read 5 elements from user store in set
s=set()
for i in range(5):
    a=int(input("enter a number"))
    s.add(a)
print(s)
#%%
# read 5 elements from user store in dict
d={}
for i in range(5):
    a=input("enter a key")
    b=input("enter a value")
    d[a]=b

print(d)
#%%
# factorial of 5
a=5
fact=1
for i in range(1,a+1):
    fact=fact*i
print(fact)
#%%
# take list and count the elements by using for loop

l=[1,2,5,3,2,8,9]
c=0

for i in l:
    c+=1
print(c)


#%%
# use while insted of for
l=[1,2,5,3,4]
c=0
i=0
while i < len(l):
    c+=1
    i+=1
print(c)
#%%
# take the list elements and print each elements by using index position

l=[10,20,30,40]
i=0
while i < len(l):
    print(l[i],end="-")
    i+=1
#%%
# tuple and reverse
# take the list elements and print each elements by using index position

l=[10,20,30,40]
i=len(l)-1
while i >= 0:
    print(l[i],end="-")
    i -= 1
#%%
# take a list and count of even number
l=[1,2,5,3,2,8,9]
c=0
for i in l:
    if i%2==0:
        c+=1
print(c)
#%%
# even index even elements count
l=[1,2,5,3,2,8,9]
c=0
for i in range(0,len(l),2):
    if l[i]%2==0:
        c+=1
print(c)
#%%
# even index odd elements count
l=[1,2,5,3,2,8,9]
c=0
for i in range(0,len(l),2):
    if l[i]!=0:
        c+=1
print(c)
#%%
# sum of list elements
l=[10,23,45,67,34]
sum=0
for i in l:
    sum+=i
print(sum)
#%%
#sum of even elemets
l=[10,23,45,67,34]
sum=0
for i in l:
    if i %2==0:
        sum+=i
print(sum)
#%%
#sum of odd elements
l=[10,23,45,67,34]
sum=0
for i in l:
    if i%2!=0:
        sum+=i
print(sum)
#%%
# take a list and print avg of numbers
l=[10,23,45,67,34]
sum=0
c=0
for i in l:
    sum+=i
    c+=1
avg=sum/c
print(avg)
#%%
# take a list and print avg of numbers inside function
def avg(l):
    sum=0
    c=0
    for i in l:
        sum+=i
        c+=1
    avg=sum/c
    return avg
a=avg([10,29,34,67,89])
print(a)
#%%
# tuple sum of odd numbers
t=(10,29,34,67,89)
sum=0
for i in t:
    if i%2!=0:
        sum+=i
print(sum)
#%%
# Tuple sum of even numbers
t=(10,29,34,67,89)
sum=0
for i in t:
    if i%2==0:
        sum+=i
print(sum)
#%%
# tuple sum of odd index odd elements
t=(10,29,34,67,89)
sum=0
for i in range(1,len(t),2):
    if t[i]%2!=0:
        sum+=t[i]
print(sum)
#%%
# tuple sum of odd index even elements
t=(10,29,34,67,89)
sum=0
for i in range(1,len(t),2):
    if t[i]%2==0:
        sum+=t[i]
print(sum)
#%%
# avg of first n natural numbers
n=int(input("enter a number"))
sum=0
for i in range (1,n+1):
    sum+=i
avg=sum/n
print(avg)
#%%
# print sum of first n natural numbers
n=int(input("enter a number"))
sum=0
for i in range (1,n+1):
    sum+=i

print(sum)
#%%
# print sum of first  n whole numbers
n=int(input("enter a number"))
sum=0
for i in range(0,n+1):
    sum+=i

print(sum)
#%%
# sum of first n even numbers
n=int(input("enter a number"))
s=0
for i in range(2,2*n+1,2):
    s=s+i
print(s)

#%%
# sum of first n odd numbers
n=int(input("enter a number"))
s=0
for i in range(1,2*n,2):
    s=s+i
print(s)

#%%
# list print avg of even numbers
l=[18,34,21,34,56]
s=0
c=0
for i in l:
    if i % 2==0:
        s+=i
        c+=1
avg = s/c
print(avg)
        
#%%
