
def calculate_average(p, m, e):
    avg = (p + m + e) / 3
    return avg


def get_scholarship(avg):
    if avg >= 80:
        return "Full Scholarship"
    elif avg >= 60:
        return "Partial Scholarship"
    else:
        return "No Scholarship"


# Take number of students
t = int(input())

for _ in range(t):

    # Take three subject scores
    p, m, e = map(int, input().split())

    # Calculate average
    avg = calculate_average(p, m, e)

    # Determine scholarship
    scholarship = get_scholarship(avg)

    # Print result
    print(f"{avg:.2f} {scholarship}")


#sample input

# 4
#90 85 95
#70 65 75
#40 50 45
#80 80 80


