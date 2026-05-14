
i = int(input("Enter the number of students: "))
student_marks = []
for j in range(i):  
    Sname=input('Enter name : ')
    Smarks = int(input("Enter marks : "))
    j ={"name":Sname,"marks":Smarks}
    student_marks.append(j)
    
for l in range(i):
    print(student_marks[l]['name'], " : ", student_marks[l]['marks'])
    
for l in range(i):
    Highest = student_marks[0]['marks']
    if student_marks[l]['marks'] > Highest:
        Highest = student_marks[l]['marks']
print("highest = ",Highest)

total = 0
for l in range(i):
    total =  total + student_marks[l]['marks']
agerage = total/i
print('Average = ',agerage)
print('Pass :')
for l in range(i):
    if student_marks[l]['marks'] >55:
        print(student_marks[l]['name'])
             