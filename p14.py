students={}
n=int(input("enter number of students:"))
for i in range(n):
    name=input ("enter student name:")
    marks=float(input("enter marks:"))
    students [name]=marks
average=sum(students.values())/len(students)
topper=max(students, key=students.get)
print("\n-----summary report-----")
print("total students:", len(students))
print("average score:", average)
print("topper:", students[topper])
print("\nstudent details:")
for name, marks in students.items():
    print(name, ":", marks)