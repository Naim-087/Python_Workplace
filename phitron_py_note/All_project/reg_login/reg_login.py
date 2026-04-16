# you have create a log in page where user can log in if they meet 4 points
#1. email 2.phone 3.username 4.password


user_data ={}

def login():
      print("___Welcome to login page__")
      user=input("Enter your name : ").strip()
      password=input("Enter password : ").strip()
      number=input("Enter phone number : ").strip()
      mail = input("Enter your mail : ").strip()
      
      if user in user_data :
            stored = user_data[user]

            if(password == stored["password"] and
               number==stored["number"] and
               mail == stored["mail"] ):
                print(f"Welcome dear {user}!\n login successfully.")
            
            else:
                  print("Invalid details..please try again")

      else:
            print("User not found")      
    
def reg():
      print("___Welcome to Regestration page__")
      user=input("Enter your name : ").strip()
      password=input("Enter password : ").strip()
      number=input("Enter phone number : ").strip()
      mail = input("Enter your mail : ").strip()
      
      user_data[user] ={
            "password" : password,
            "number" : number,
            "mail" : mail
      }
      print("Regestration successfully...")
       
      

print("_____Welcome to System_____")
while True:
      print("1.Registration\n2.Login\n3. Exit")
      try:
                 
                 choice=int(input("Enter your choice : "))
                 if(choice== 1):
                   print("Redirected to Regestration... ")
                   reg()

                 elif(choice==2):
                        print("Redirected to Login... ")
                        login()
                 elif(choice==3):
                       print("Exit")

                 else:
                       print("Invalid choice...")
                       break

                         
      except ValueError:
            print("Enter a valid number.")
             
        
      

            
       
    
      