name=input("Enter Student Name : ")
student_id=input("Enter Student ID : ")
department=input("Enter Department : ")

subjects=['Python','Math','English','Physics','ICT']
marks={}
print("\n Enter Subject Marks (0-100): ")
for subject in subjects:
    while True:
        mark=float(input(f"{subject}: "))
        if mark<0 or mark>100:
            print("Please enter marks between 0 and 100")
            continue
        else:
            marks[subject]=mark
            break

total=sum(marks.values())
average=total/len(subjects)
highest=max(marks.values())
lowest=min(marks.values())

if average>=80:
    grade="A+"
elif average>=70:
    grade="A"
elif average>=60:
    grade="A-"
elif average>=50:
    grade="B"
elif average>=40:
    grade="C"
else:
    grade="F"

status="Passed"

for mark in marks.values():
    if mark<40:
        status="Failed"
        break

correct_password="Shihab123"

while True:
    password=input("\nEnter Password : ")
    if password==correct_password:
        print("Password Correct!\n")
        break
    else:
        print("Wrong Password! Try Again.")

print("===== String Operations =====")
print("UpperCase : ",name.upper())
print("LowerCase : ",name.lower())
print("Length : ",len(name))
print("Frist 3 : ",name[:3])
print("Last 3 : ",name[-3:])

sports={"Football","Cricket","Badminton"}
clubs={"Programing","Cricket","Photography"}

print("\n===== Set Operations =====")
print("Common Items : ",sports.intersection(clubs))
print("Unique Items : ",sports.union(clubs))

weekdays=(
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday"
)

print("\n===== Tuple Example =====")
print("Frist day : ",weekdays[0])
print("Last day : ",weekdays[-1])
print("Total days : ",len(weekdays))

passed_subjects=[subject for subject,mark in marks.items() if mark>=40]

print("\n==============================")
print("      STUDENT REPORT")
print("==============================")
print(f"Name  :  {name}")
print(f"ID    : {student_id}")
print(f"Department : {department}")

for subject in subjects:
    print(f"{subject:<10}:{marks[subject]}")

print("------------------------------")
print(f"Total    : {total}")
print(f"Average  : {average}")
print(f"Highest  : {highest}")
print(f"Lowest   : {lowest}")
print(f"Grade    : {grade}")
print(f"Status   : {status}")
print(f"Pass Subject   : {passed_subjects}")

print("==============================")