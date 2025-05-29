def doc_function():
    """This function does something that is well documented"""
    print("This is only for the document")

print(doc_function.__doc__)
another_fn = doc_function
print(another_fn.__doc__)

def student_details(name, school, math, physics, chemistry, biology, enrolled=False):
    total = math + physics + chemistry + biology
    print("Name:", name)
    print("School:", school, "Enrolled:", enrolled)
    print("Total Score:", total)

student_details("Devid", "Germany", 90, 34, 56, 89, enrolled="Yes")
student_details("Jhon", "Irland", 90, 34, 43, 89)

def students_in_collage(collage, city,*student):
    print("Collage:",collage)
    print("City:",city)
    print("Student:",student)
students_in_collage("Gryffindor", "London","Devid","Melan","Jhon")

def student_in_collage(*student,collage="Standford",city="California"):
    print("Collage:",collage)
    print("City:",city)
    print("Student:",student)
student_in_collage("Nolen","Elsa","Devid")

def students_details(**kwargs):
    print(type(kwargs))
    print(kwargs)
students_details(Name="Jhon",Age=21)

def student_details(**details):
    for key, value in details.items():
        print(key,value)
student_details(Name="Devid Melan",Age="21",City="London",University="Gryffindor")

def student1_details(**details):
    if 'name' in details:
        print("Name:", details['name'])
    if 'age' in details:
        print("Age:", details['age'])
    if 'collage' in details:
        print("Collage:", details['collage'])
student1_details(name="Jhone Cloud", age=21, collage="London")

