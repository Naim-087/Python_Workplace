def letterMark_function (scores):
    return scores >=80


scores= [40,88,90,80,56,77,81,91]

result = filter(letterMark_function,scores)

print(list(result))

