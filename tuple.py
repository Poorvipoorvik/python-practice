t=(10,20,30,40)

#access element is possible
print(t[1])
t +=(50,)
print(t)

#modify
t[1] =15      # error
print(t)

# adding element to position
t[0] += 10   #error
print(t)

# delete
del t[2]   #error
print(t)