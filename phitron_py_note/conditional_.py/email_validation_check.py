print('''
      ___Email Validation Check___
      1.Must not be empty
      2.Must contain'.' and '@'
      3.Must contain exactly one '@'
      4.Must end with '.com ,.org, .net'
      5.Must start and end with a letter or a digit
      6.No longer than 50 words.

      ''')

mail = input("Enter your Email : ").strip()

if mail =="":
    print("Email can not be empty")

elif not ('.' in mail and '@' in mail): # import 'not' use 
    print("Must contain . and @ ")

elif (mail.count('@') > 1 ):
    print("Must contain exactly one '@' ")

elif not (mail.endswith(('.com','.org','.net'))):

    print("Must end with .com .org .net")

elif not (mail[0].isdigit() or mail[0].isalpha() or mail[-1].isalpha() or mail[-1].isdigit()):
    print("Must start and end with a letter or a digit")


elif(len(mail)>50):

    print("No longer than 50 words.")
else:
    print("Valid Mail ")




