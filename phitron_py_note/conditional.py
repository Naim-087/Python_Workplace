num1=float(input("Enter the first number : "))
num2=float(input("Enter the second number : "))
print("Which operations you want to : ")
print("1.addition ")
print("2.substraction ")
print("3.multiplication ")
print("4.division ")
choice =int(input("Enter Your Choice : "))

if choice==1 :
    print("add = ",num1+num2)
elif choice==2 :
    print("Sub =",num1-num2)
elif choice ==3 :
    print("Multi =",num1*num2)
elif choice==4 :
    print("Div =",num1/num2)
else :
    print("Invalid choice .")