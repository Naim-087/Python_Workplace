print("Hollow Rectangle Pattern :")
def hollow_rectangle(total_rows, total_colums ) :
    for i in range(total_rows) :
        for j in range(total_colums) :
            if i==0 or i==total_rows-1 or j==0 or j== total_colums-1 :
                print("*",end=" ") 
            else:
                print(" ",end=" ")
        print()

hollow_rectangle(4,5)