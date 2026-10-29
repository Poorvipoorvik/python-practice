def patient(name,*disease,bg,email="none"):
    print(name)
    print(bg)
    print(disease)
    print(email)
patient("poorvik","cold","fever",bg="o-ve")


print("----------------------------------------------------------------------------------------------------------------")


# 2nd 

def student(name,*gmail,age,**address):
    print(name)
    print(age)
    print(gmail)
    print(address)
student("poorvik","poorvik@gmail.com","varch@gmail.com",age=30,city="hassan",pincode=573131,phno=646367)
student("poo","varch@gmail.com",age=18,pincode=573131,phno=646367)


print("--------------------------------------------------------------------------------------------------------------------------")

# 3rd 

def person(name,age,place="hassan"):
    print("name : ",name)
    print("age : ",age)
    print("place : ",place)
person("poorvik",21,place="bangaluru")
person('poorvik',age=22)


print("--------------------------------------------------------------------------------------------------------------------------------------")

# 4th

def student(name,course="BCA", **subjects):
    print(name)
    print(course)
    print(subjects)
student("poorvik",kan=50,eng=80)


print("-------------------------------------------------------------------------------------------------------------------------")


# 5th

def student(batch_name,*hobbies,name,**marks):
    print(batch_name)
    print(name)
    print(hobbies)
    print(marks)
student("aliens","tennis","cricket",name="suresh",java=24,python=25,computers=23)

print("------------------------------------------------------------------------------------------------------------------------------")

#6th

def collage(proff_name,proff_dept,**subject_knowladge):
    print(proff_name)
    print(proff_dept)
    print(subject_knowladge)
collage("govind",proff_dept="computer science", data_structure="30%",mathamatics="70%")