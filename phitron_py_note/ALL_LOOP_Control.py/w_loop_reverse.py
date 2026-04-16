num=int(input("Enter a Number : "))

sum=0


while num>0 :
    single_digit=num%10 
    sum=sum*10+single_digit
    num=num//10
    
   
    

print(sum)