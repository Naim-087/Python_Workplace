def find_median(sorted_list):
    n = len(sorted_list)
    middle = n // 2
    if n % 2 == 1:                  # odd count: take the middle item
        return sorted_list[middle]
    return (sorted_list[middle - 1] + sorted_list[middle]) / 2   # even: average the two middle items


def find_outliers(values):
    data = sorted(values)           # step 1: sort the data
    n = len(data)
    half = n // 2

    lower_half = data[:half]        # step 2: split into lower and upper halves
    if n % 2 == 1:
        upper_half = data[half + 1:]    # odd count: skip the middle item
    else:
        upper_half = data[half:]

    q1 = find_median(lower_half)    # step 3: quartiles
    q3 = find_median(upper_half)
    iqr = q3 - q1

    lower_fence = q1 - 1.5 * iqr    # step 4: fences
    upper_fence = q3 + 1.5 * iqr

    outliers = []                   # step 5: collect values outside the fences
    for v in values:
        if v < lower_fence or v > upper_fence:
            outliers.append(v)
    return outliers


print(find_outliers([3, 5, 7, 8, 9, 11, 13, 15, 40]))   # [40]
print(find_outliers([1, 2, 3, 4, 5, 100]))              # [100]
print(find_outliers([10, 12, 11, 13, 12]))              # []


    