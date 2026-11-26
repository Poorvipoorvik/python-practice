#%%
l=[10,34,57,"hrllo",90]
l1=[i for i in l]
print(l1)
#%%
# print all even numbers store in list 

l=[10,11,1,9,12,14,16]
l1=[ i for i in l  if i%2==0]
print(l1)
#%%
# print if even ="hi" odd ="hello"

l=[10,11,1,9,12,14,16]
l1=["hi" if i%2==0 else "hello" for i in l  ]
print(l1)
#%%
s="good morning"
s1=[]
for i in s:
    if i in "aeiouAEIOU":
        s1.append(1)
    else:
        s1.append(0)
print(s1)
#%%
# store vowel as 1 and consonents as 0 in the list
s="good morning"
s1=[1  if i in "aeiouAEIOU " else 0 for i in s]
print(s1)
#%%
# using list compresion store elements 1to 10
l=[i for i in range(1,11)]
print(l)
#%%
# odd index even elemets

l = [10, 11, 1, 9, 12, 14, 16]
l1=[l[i]  for i in range(1,len(l),2) if l[i]% 2==0]
print(l1)
#%%
# if the elements is even then store the square of its or then store same as it

l=[10,13,24,1,6,56,78,98,34]
l1=[i**2 if i%2==0 else i for i in l]
print(l1)
#%%
