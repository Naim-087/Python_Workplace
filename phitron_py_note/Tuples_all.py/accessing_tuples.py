'''
Tuples are unchangable , but there is a workaround .
1.first convert tuple into list
2. change the list 
3. then convert changed list into tuples again


'''
sub_cgpa =(("OOp",4.00),("Algorithm",4.00),("Robotics",4.00),("Accounting",4.00))


new_sub_cg = list(sub_cgpa)

print(new_sub_cg)

new_sub_cg [3] = ["OOp Lab",4.00]
print(new_sub_cg)

my_final_tup = tuple(new_sub_cg)

print(my_final_tup)

print(type(my_final_tup))


