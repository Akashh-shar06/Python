num1 = int(input("Enter The Age :"))

if (num1 > 0 and num1 <=18):
    print("Teenager")
elif(num1 > 19 and num1 <=30):
    print("Adult")
elif(num1 > 31 and num1 <=60):
    print("Men's")
elif(num1 > 61 and num1 <=100):
    print("Senior")
else:
    print("Not Found !!!")
