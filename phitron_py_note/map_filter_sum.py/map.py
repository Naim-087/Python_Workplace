"""
map() is a built-in function in Python that applies a given function to each element of an iterable (such as a list, tuple, or set) 
and returns an iterator containing the results.
"""
#map() applies a function to every element of a sequence.

celsius = [0, 10, 20, 30, 40]

def to_fahrenheit(temp):
    return (temp * 9/5) + 32

fahrenheit = list(map(to_fahrenheit, celsius))
print(fahrenheit) # [32.0, 50.0, 68.0, 86.0, 104.0]