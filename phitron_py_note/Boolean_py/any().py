print(any([False, False, True]))    # True
print(any([False, False, False]))   # False
print(any([0, 0, 5]))               # True (5 = True)
print(any([0, 0, 0]))               # False
print(any([]))                      # False (empty iterable)