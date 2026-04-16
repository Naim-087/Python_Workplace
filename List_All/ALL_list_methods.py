#methods
list =[30,99,"Apple","Banana","Mangoes",10,90,40.78,["Pain","Safin"]]
print(list)

#changing list object
list[3]=8
list[8]="YES/No"
list[6]="Buddy"
print("\nAfter mutataing list object\n ")
print(list)
print("\n")

#Slicing list
new_list=list[0:4]
new_list2=list[3:6]
new_list3=list[2:8]
print(new_list3)
print(new_list)
print(new_list2)

#Append()
list.append("Orange")
print("Appended",list)
print("\n")

#Copy()
list2=list.copy()
print("Copied list",list2)
print("\n")

#Insert(pos,object)

list2.insert(6,"Apple")
list2.insert(8,"Apple")
print("Inserted list",list2)
print("\n")

#Count(object)
x=list2.count("Apple")
print("Counted " ,x)
print("\n")

#Index (object), (object,start,end)
x=list2.index("YES/No")
print("Index No. ",x)
print("\n")

#Reverse The List
list2.reverse()
print("Reversed List ",list2)
print("\n")

#Sort the List
#list.sort(), allows only same data typed list , mixed data type list cant be sorted

#Clear the list
list2.clear()
print("Cleared List",list2)
print("\n")






