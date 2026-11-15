
def calculate_result(marks):
    total = sum(marks)
    average = total / len(marks)
    status = "Passed" if all(mark >= 40 for mark in marks) else "Failed"

    return total, average, status


def get_student_data(n):
    students = []

    for _ in range(n):
        data = input().split()

        name = data[0]
        marks = list(map(int, data[1:]))

        total, average, status = calculate_result(marks)

        student = {
            "name": name,
            "marks": marks,
            "total": total,
            "average": average,
            "status": status
        }

        students.append(student)

    return students


def analyze_students(students):

    # Sort students by total marks (descending)
    ranked_students = sorted(
        students,
        key=lambda student: student["total"],
        reverse=True
    )

    print("\nStudent Results:\n")

    for student in ranked_students:
        print(
            f'{student["name"]}: '
            f'Total = {student["total"]}, '
            f'Average = {student["average"]:.2f}, '
            f'{student["status"]}'
        )

    # Find top student
    top_student = ranked_students[0]
    print(f'\nTop Student: {top_student["name"]}')

    # Find high achievers
    high_achievers = [
        student["name"]
        for student in ranked_students
        if student["average"] >= 80
    ]

    print("High Achievers:", ", ".join(high_achievers))


# Main program
n = int(input())
students = get_student_data(n)
analyze_students(students)
