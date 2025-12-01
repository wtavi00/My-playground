def doc_function():
    """This function does something that is well documented"""
    print("This is only for the document")

print(doc_function.__doc__)
another_fn = doc_function
print(another_fn.__doc__)

def student_details(name, school, math, physics, chemistry, biology, enrolled=False):
    """student_details("Devid", "Germany", 90, 34, 56, 89, enrolled="Yes")
    student_details("Jhon", "Irland", 90, 34, 43, 89)"""
    
    total = math + physics + chemistry + biology
    print("Name:", name)
    print("School:", school, "Enrolled:", enrolled)
    print("Total Score:", total)

def students_in_collage(collage, city,*student):
    """students_in_collage("Gryffindor", "London","Devid","Melan","Jhon")"""
    print("Collage:",collage)
    print("City:",city)
    print("Student:",student)

def student_in_collage(*student,collage="Standford",city="California"):
    """student_in_collage("Nolen","Elsa","Devid")"""
    print("Collage:",collage)
    print("City:",city)
    print("Student:",student)

def students_details(**kwargs):
    """students_details(Name="Jhon",Age=21)"""
    print(type(kwargs))
    print(kwargs)
    
def student_details(**details):
    """student_details(Name="Devid Melan",Age="21",City="London",University="Gryffindor")"""
    for key, value in details.items():
        print(key,value)

def student1_details(**details):
    """student1_details(name="Jhone Cloud", age=21, collage="London")"""
    if 'name' in details:
        print("Name:", details['name'])
    if 'age' in details:
        print("Age:", details['age'])
    if 'collage' in details:
        print("Collage:", details['collage'])

a_list=[43,4,56,8,89321,3,34,52,62,564,673,54,65,56545]
b_list=[2,3,4,56,7,8,9,1,10,12,13,14]
cars_list=["toyota","tata","mazda","bmw"]

def length(some_list):
    count=0
    for i in some_list:
        count +=1
    print("The length of the list is", count)
    return count

def finde_max_in_list(some_list):
    max_element =  some_list[0]
    length = len(some_list)
    for i in range(1,length):
        if some_list[i] > max_element:
            max_element=some_list[i]
    return max_element

def finde_max(some_list):
    count= max(some_list)
    return count

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
    
def max_in_empty(some_list):
    if len(some_list)==0:
        print("No element presents")
        return None
    count=max(some_list)
    print("This is",count)
    return count

def finde_first_capital(some_string):
    capital_letter = None
    for ch in some_string:
        if ch.upper() == ch and ch != " ":
            capital_letter= ch
            break
    if capital_letter is None:
        return "No capital letters found"
    else:
        return "First capital letter: " + capital_letter

def create_dictionary_intro(name, age, job):
    dictionary={
        "Name": name,
        "Age": age,
        "Job": job
    }
    return dictionary

