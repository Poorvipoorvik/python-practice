# 1st read a age and gender from user if age grater then or equal to 18 and gender is male  he is eligible for vote otherwise age graterthan or equal to 
# to 18 and gender is female she is eligible for vote otherwise invalid gender

age=int(input("enter a  age"))
gender=input("enter a gender")

if age>=18 and gender=="male":
    print("he is eligible for vote")
elif age>=18 and gender=="female":
    print("she is eligible for vote")
else:
    print("invaild gender")

print("#################################################################################################################33")

# read a season from user if season is summer then print very hot otherwise season is  rainy print carry unberella otherwise season is winter print colde otherwise print 
#invaild season

season=input("enter a season")
if season=="summer":
    print("its very hot")
elif season=="rainy":
    print("carry umbrella")
elif season=="winter":
    print("cold")
else:
    print("invaild season")
