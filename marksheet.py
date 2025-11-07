# Basic information
name = input("Enter your name: ")
rollNum = input("Enter your Roll number: ")
claSS = input("Enter your class: ")

#Subject marks
marksOb = 0
noSub = int(input("Enter number of Subjects: "))

for i in range(noSub):
  marks = float(input(f"Enter marks of Subject {i + 1}: "))
  marksOb += marks

#Total marks assuming each subject is out of 100
total = noSub * 100

# Calculates percentage
per = ( marksOb / total ) * 100

#Grade decision 
grade = (
  "A1" if per >= 90 and per <= 100 else 
  "A" if per >= 80 and  per <= 89 else
  "B" if per >= 70 and per <= 79 else
  "C" if per >= 60 and per <= 69 else
  "D" if per >= 50 and per <= 59 else
  "Fail"
)

#Marksheet Structure
print(f"\n\n\t\tMarksheet of {name}")
print(f"\t\t**********************\n\n")

print(f"\tname of student: {name}")
print(f"\tRoll number of student: {rollNum}")
print(f"\tClass of student: {claSS}\n")
print(f"\tMarks Obtained: {marksOb}")
print(f"\tPercentage: {per:.2f} %")
print(f"\tGrade: {grade}\n")









