#making a even list from 0-100 with loop

even=[]
for x in range(101) :
    if x%2==0 :
        even.append(x)

print(even)     
print("\n")
#With list copmrehension 
even=[x for x in range(101) if x%2==0]
print(even)
print("\n")

fruits = ["apple", "banana", "cherry", "kiwi", "mango","orange","jackfruits","lemon"]

new_list=[x for x in fruits if "a" in x]
print("a contended fruits ",new_list)
print("\n")

nl2=[x for x in fruits if x!="apple" and x!="lemon"]
print("Denied apple and lemon",nl2)
print("\n")







