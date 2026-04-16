
num=int(input("Enter a number : "))
rest_digit=num
sum=0
while rest_digit>0 :
    last_digit=(rest_digit%10)
    sum=sum + last_digit 
    rest_digit=rest_digit //10
   
print(sum)
    

