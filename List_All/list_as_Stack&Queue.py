numbers=[99,5,87,15,77,89,95,103,43,55,23,19]

#sort (ascending)
numbers.sort()
print("\nAscending Sorted Number : ",numbers)
print("\n")
#sort (descending)
numbers.sort()
numbers.reverse()
print("Descending Sorted Number : ",numbers)
print("\n")


#Stack

stack=[]
print(type(stack))

#stack push
stack.append(23)
stack.append(16)
stack.append(9)
stack.append(30)
stack.append(60)
stack.append(44)

#stack pop- first in last out
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print("\n")

#QUEUE

queue=[]

queue.append(3) #insert
queue.append(1)
queue.append(30)
queue.append(43)
queue.append(98)
queue.append(6)

#remove 
print(queue.pop(0))
print("Front e ache ",queue[0]) #track the first element

print(queue.pop(0))
print("Front e ache ",queue[0]) #track the first element

print(queue.pop(0))
print("Front e ache ",queue[0]) #track the first element

