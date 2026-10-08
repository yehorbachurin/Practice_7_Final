INPUT_FILE = "students.csv"
OUTPUT_FILE = "result.txt"

math_points_sum: float = 0.0
python_points_sum: float = 0.0
english_points_sum: float = 0.0
students_count: int = 0
average_points: float = 0.0
best_student: tuple[str, float] | None = None

with open(INPUT_FILE, "r", encoding="utf-8") as file:
    next(file)

    for line in file:
        data = line.strip().split(",")


        name = data[0]
        math = int(data[1])
        python = int(data[2])
        english = int(data[3])

        math_points_sum += math
        python_points_sum += python
        english_points_sum += english

        students_count += 1

        average_point = (math + python + english) / 3

        if best_student is None:
            best_student = (name, average_point)
        else:
            best_student_name, best_student_average_score = best_student

            if average_point > best_student_average_score:
                best_student = (name, average_point)

average_point = (math_points_sum + python_points_sum + english_points_sum) / 3

with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
    best_student_name, best_student_average_score = best_student

    output = (
        "Середній бал по класу:\n"
        f"math: {math_points_sum/students_count:.1f}\n"
        f"python: {python_points_sum/students_count:.1f}\n"
        f"english: {english_points_sum/students_count:.1f}\n\n"
        f"Найкращий студент: {best_student_name} ({best_student_average_score:.1f})"
    )
    file.write(output)
    print(output)



