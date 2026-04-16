print(all([True, True, True]))      # True
print(all([True, False, True]))     # False
print(all([1, 2, 3]))               # True (non-zero = True)
print(all([1, 0, 3]))               # False (0 = False)
print(all([]))                      # True (empty iterable)

