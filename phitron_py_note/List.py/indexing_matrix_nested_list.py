matrix = [['Ruby','Go','Python'],
          ['Rails','Go_in','FastApi'],
          ['Html','CSS','React']]

print(matrix)

'''col     0    1    2
        _|____________________
row    0 | 0,0   0,1  0,2
         |
       1 |1,0    1,1  1,2
         |
       2 | 2,0    2,1  2,2


'''

#Find out Go and CSS

print(f"Go is found = {matrix[0][1]} and CCS is found = {matrix[2][1]}")