students = {}

try:
    n = int(input("Enter number of students: "))
    
    for i in range(n):
        name = input("Enter student name: ")
        marks = []
        
        for j in range(3):
            mark = int(input(f"Enter mark {j+1}: "))
            marks.append(mark)
        
        students[name] = marks

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

except ValueError:
    print("Please enter valid numbers only!")
