# Typecasting = the process of converting a variable from one data to another
#               str(), int(), float(), bool()
name = "Agbenisi Ayomide"
Age = 19
GPA = 5.0
is_student = False
school = "Lagos state university"

print(type(name))
print(type(Age))
print(type(GPA))
print(type(is_student))

GPA = int(GPA)
print(GPA)

name = str(name)
print(name)

Age = float(Age)
print(Age)

is_student = bool(is_student)
print(is_student)

Age = str(Age)
print(type(Age))
Age += "1"

print(Age)

name = bool(name)
print(name)
print(type(school))
school = str(school)
