def calculate_average(score1, score2, score3):
    return (score1 + score2 + score3) / 3

def result_status(average):
    if average >= 50:
        return "Pass"
    return "Fail"

def assign_grade(average):
    if average >= 70:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"

def result_summary(name, average, grade, status):
    return f"{name} scored an average of {average}. Grade: {grade}. Status: status." 

name = "Ada"
average = calculate_average(70, 80, 90)
status = result_status(average)
grade = assign_grade(average)
summary = result_summary(name, average, grade, status)

print(summary)
