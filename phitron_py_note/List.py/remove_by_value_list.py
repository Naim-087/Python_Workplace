matrix =[
    ['a','b','c'], # Row 0
    ['d','e','f'], # Row 1
    ['g','h','i']  # Row 2
]

for row in matrix:
    if 'e' in row:
        row.remove('e')
        
print(matrix)



