'''*args and **kwargs allow functions to accept 
a unknown number of arguments.'''

def Sum(*args):
    print(sum(args))

Sum(23,1,4)
Sum(2,12)
Sum(39,1,66,90)

