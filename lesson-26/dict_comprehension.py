names = ["any", "names"]
student_score = {student:random.randint(1, 100) for student in names}


passed_students = {student:score for (student, score) in student_score.items() if score >= 60}
