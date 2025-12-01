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

a_list=[43,4,56,8,89321,3,34,52,62,564,673,54,65,56545]
b_list=[2,3,4,56,7,8,9,1,10,12,13,14]
cars_list=["toyota","tata","mazda","bmw"]

def length(some_list):
    count=0
    for i in some_list:
        count +=1
    print("The length of the list is", count)
    return count

a=length(a_list)
print(a)
length(cars_list)

def finde_max_in_list(some_list):
    max_element =  some_list[0]
    length = len(some_list)
    for i in range(1,length):
        if some_list[i] > max_element:
            max_element=some_list[i]
    return max_element
z=finde_max_in_list(a_list)
print(z)


def finde_max(some_list):
    count= max(some_list)
    return count
x= finde_max(b_list)
print(x)

empty_list=[]
def finde_max_in_list(some_list):
    if len(some_list)==0:
        print("Zero element list")
        return None
    max_element=some_list[0]
    length=len(some_list)
    for i in range(1,length):
        if some_list[i]>max_element:
            max_element=some_list[i]
    return max_element

c=finde_max_in_list(empty_list)
print(c)
d=finde_max_in_list(a_list)
print(d)

def max_in_empty(some_list):
    if len(some_list)==0:
        print("No element presents")
        return None
    count=max(some_list)
    print("This is",count)
    return count
max_in_empty(a_list)
e=max_in_empty(empty_list)
f=max_in_empty(a_list)
print(f)
