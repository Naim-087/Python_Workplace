print("a"=="b") # check their ascii value

print("___welcome____")
print('''
1. your user name must be : small letter a-z
2. your password must be/: 1-9 
3.password not less than 5 ''')

user=input("Enter your username : ")
password = input("Enter your password : ")

user1=True
pass1=True

for ch in user :
   if not (ch >='a' and ch <='z'): #"If ch is NOT between 'a' and 'z'"
        user1=False  # jodi na hoy a-z then user false
        break
        
for ch in password :
    if not (ch>='1' and ch<='9'):
        pass1=False
        break


if(user1  and pass1 ): #defualt if they are both true
    print("Log in Successfull !!!")
else:
    print("Invalid credentials ")
        
      
      

