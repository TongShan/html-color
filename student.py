lloyd = {
    "name": "Lloyd",
    "homework": [90, 97, 75, 92],
    "quizzes": [88, 40, 94],
    "tests": [75, 90]
}

alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}

tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

def average(lst):
    average = float(sum(lst)) / len(lst)
    return average

def get_average(student):
    student_average = average(student['homework']) * 0.1 + average(student['quizzes']) * 0.3 + average(student['tests']) * 0.6
    return student_average

def get_letter_grade(score):
    if score >= 90:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score <70:
        return 'D'
    else:
        return 'F'


print get_letter_grade(get_average(lloyd))
