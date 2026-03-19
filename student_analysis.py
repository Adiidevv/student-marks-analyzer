students = {
    "Rahul": [85, 78, 92],
    "Anjali": [90, 88, 95],
    "Arjun": [70, 75, 80]
}

def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    else:
        return "C"

top_student = ""
highest_avg = 0

for name, marks in students.items():
    total = sum(marks)
    avg = total / len(marks)
    grade = calculate_grade(avg)

    print(f"{name} -> Total: {total}, Average: {avg:.2f}, Grade: {grade}")

    if avg > highest_avg:
        highest_avg = avg
        top_student = name

print(f"\nTop Student: {top_student}")