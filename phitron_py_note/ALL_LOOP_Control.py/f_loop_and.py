print("Numbers from 1 to 20 which are not divisible by 2, 3 and 5")
sum=0
for i in range(1,20,1) :
    if i%2!=0 and i%3!=0 and i%5!=0 :
        print(i,end=' ')
        sum=sum+i

print(' ',sum)