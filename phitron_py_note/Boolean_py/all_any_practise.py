#Collections to test
true_list = [True, 1, "Hello"]    # All values have content (truthy)
mixed_list = [True, 0, "Hello"]   # 0 is considered False (falsy)
false_list = [False, 0, ""]       # All are empty/zero (falsy)

# 1. Using all() - Needs everything to be True
print(all(true_list))   # Output: True
print(all(mixed_list))  # Output: False (because of the 0)

# 2. Using any() - Needs at least one True
print(any(mixed_list))  # Output: True (because True and "Hello" are there)
print(any(false_list))  # Output: False (nothing is true)