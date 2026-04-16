nums =[1,4,9,16,25,36,49,64,81,100]
i=0

fond=0
while i<len(nums) :
    if(nums[i]==49):
        fond=1
        break
    i=i+1

if(fond==1) :
    print("Fond at ",i)
else :
    print("Not Found")

    