# list can store mixed type values
#automatically grows and shrink
#list doesnt store the actual values it stores a reference 
#[where the object lives in memory]

#method 1
List=list(["a",10,"banana"])
print(List)
List =["Apple","Banana","Mangoes",10,90,40.78,["Pain","Safin"]]
print(List)
print(type(List))