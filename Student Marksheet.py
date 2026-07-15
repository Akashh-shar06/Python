Name = input("Student Name :")
English = int(input("Enter the english Marks :"))
Hindi = int(input("Enter the hindi Marks :"))
Marathi = int(input("Enter the marathi Marks :"))
Maths = int(input("Enter the maths Marks :"))
Science = int(input("Enter the Science Marks :"))

total = English + Hindi + Marathi + Maths + Science 
percentage =  (total / 500.0) * 100

print("percentage" , percentage)

if(percentage > 90):
    print("O Grade ")
elif(percentage > 80):
    print("A Grade ")
elif(percentage > 70):
    print("B Grade ")
elif(percentage > 60):
    print("C Grade ")
elif(percentage > 50):
    print("D Grade ")
else:
    print("Fail")


