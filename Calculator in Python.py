num1 = int(input("Enter the value : "))
num2 = int(input("Enter the value : "))

print("Menu")
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")

choice = int(input("Enter the Choice(1-5) : "))

match choice:
    case 1:
        print("Addition =" , num1+num2)
    case 2:
        print("Substraction =" , num1-num2)
    case 3:
        print("Multiplication =" , num1*num2)
    case 4:
        if num2 != 0:
            print("Division =" , num1/num2)
        else:
            print("!!! Error !!")
    case 5:
        if num2 != 0:
            print("Modulus =" , num1%num2)  
        else:
            print("!! Error !!")
    case _ :
        print("Value Not Found ")
