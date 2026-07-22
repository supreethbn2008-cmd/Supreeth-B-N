print("WELCOME TO GRADE CALCULATOR")
print()
student_name = input("enter the name of the student: ")
print()
print("HELLO ", student_name)
print()
x=int(input("enter the marks of 1st language: "))
y=int(input("enter the marks of 2nd language: "))
z=int(input("enter the marks of PHYSICS : "))
l=int(input("enter the marks of CHEMISTRY : "))
m=int(input("enter the marks of MATH : "))
n=int(input("enter the marks of ELECTRONIS : "))
print()
g=x+y+z+l+m+n
print("TOTAL MARKS OBTAINED BY ", student_name, " IS : ", g)
print()
print("and grade")
if g>=510:
    print("Distinction")
    print("pass")
elif g>=450 and g<510:
    print("First Division")
    print("pass")
elif g>400 and g<450:
    print("Second Division")
    print("pass")
elif g>=350 and g<400:
    print("Third Division")
    print("pass")
elif g>=200 and g<350:
    print("pass")
else:
    print("fail")
print()

    