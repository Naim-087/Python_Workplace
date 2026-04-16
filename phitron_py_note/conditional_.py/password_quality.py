print('''
      ___Email Validation Check___
      1.Must not be empty
      2.Must be at least 8 character
      3.Must include at least 1 upper case
      4.Must include at least 1 lower case
      5.Must not be same as mail
      6.Must not contain any space
      7.Must starts and ends with a letter or digit


      ''')

mail = input("Enter your email : ").strip()
password = input("Enter your password : ").strip()

if password == "":
    print("Empty password ")

elif len(password)<8 :
    print("Must be at least 8 character ")

elif password == password.upper()  :
    print("Must contain at least 1 lower case ")

elif password == password.lower() :
    print("Must contain at least 1 upper case ")


elif password == mail :
    print("Must not be same as mail ")

elif " " in password :
    print("Must not be any space ")

elif not password[0].isdigit() and password[0].isalpha() :
    print("Must starts with a letter or digit ")

elif not password[-1].isdigit() and password[-1].isalpha() :
    print("Must starts with a letter or digit ")

else :
    print("Strong password ")
