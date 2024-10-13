# data = []

with open("students_subjects_marks.csv", 'r') as file:
    header = file.readline().strip().split(',')
    # data.append(header)


    
    subject_marks = {}
    student_total = {}
    student_subject_marks = {}

    for line in file:
        student_name, subject, marks = line.strip().split(',')
        marks = int(marks)


        if subject not in subject_marks:
            subject_marks[subject] = []
        subject_marks[subject].append(marks)


        if student_name not in student_total:
            student_total[student_name] = 0
        student_total[student_name] = student_total[student_name] + marks
        

        if student_name not in student_subject_marks:
            student_subject_marks[student_name] = {}
        student_subject_marks[student_name][subject] = marks

# print(subject_marks,'\n\n', student_total, '\n\n',  student_subject_marks)


def calculate_median(values):
    sorted_values = sorted(values)
    n = len(sorted_values)
    mid = n // 2
    
    if n % 2 == 0:
        return (sorted_values[mid - 1] + sorted_values[mid]) / 2
    else: 
        return sorted_values[mid]


# average marks of each subject
# print(subject_marks.items())
for subject, marks in subject_marks.items():
    avg_marks = sum(marks) / len(marks)
    print('Avg Marks of', subject, ' ---> ', avg_marks)  


    max_marks = max(marks)
    print('Max Marks of', subject, '---> ', max_marks)


    subject_median_marks = calculate_median(marks)
    print('Median Marks of', subject, '---> ', subject_median_marks)


# total marks of each student
for student_name, marks in student_total.items():
    print('Total Marks of', student_name, '---> ', marks)
        



#topper
topper = max(student_total, key = student_total.get)
print(f" Overall Topper: {topper} with total marks of {student_total[topper]}")


# topper of each subject

# print(student_subject_marks.items())

for subject in student_subject_marks['John Doe']:
    highest_marks = -1
    toppers = []

    for student_name, marks in student_subject_marks.items():
        if marks[subject] > highest_marks:
            highest_marks = marks[subject]
            toppers = [student_name]
        elif marks[subject] == highest_marks:
            toppers.append(student_name)
    
    # Display the topper(s) for the subject
    print(f"{subject} Topper is: {', '.join(toppers)} with {highest_marks} marks")


# median marks of each student
student_marks = []
for student_name, subject in student_subject_marks.items():
    # student_marks.append(subject.values())
    student_marks = list(subject.values())  # Extract the marks for all subjects of the student
    student_median_marks = calculate_median(student_marks)
    print(f"median marks of {student_name} : {student_median_marks}")





    




