print('f' in 'python')

print(3 not in [2,4,5,8])

#security check : ensure domain validations

domain = "@edu.bd"

banned_domain = ["@spam.com","@fake.org","@gmail.com","@bot.net"]

if(domain not in banned_domain) :
    print("Login Successfull")
    
