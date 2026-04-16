char = input("Enter any character : ")

if(char.isalpha()):
 print("You entered a charcter.")
elif(char.isdigit()) :
 print("You entered a digit.")
elif(char.isascii()) :
 print("You enteres a ascii.")
elif(char.isspace()) :
 print("You entered a space.")
elif(char.isdecimal()) :
 print("You entered a decimal.")
else:
 print("Invalid character .")

 
  