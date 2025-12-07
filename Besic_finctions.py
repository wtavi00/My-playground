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
    """i=create_dictionary_intro(name="Jhon", age=25, job="Student")"""
    dictionary={
        "Name": name,
        "Age": age,
        "Job": job
    }
    return dictionary

def score_total():
    math=float(input("Math score:"))
    physics=float(input("Physics:"))
    chamistry=float(input("Chemistry:"))
    biology=float(input("Biology:"))
    total=math+physics+chamistry+biology
    print("Math:",math, "Physics:",physics, "Chamistry",chamistry, "Biology",biology,"Total:", total)
    return total

def print_fn(*args):
    args_type= type(args)
    print(args_type)
    print(args)

def s_details(**kwargs):
    """This doble * means that this function will invoke the value in dectionary{}
    s_details(Name="Jhon",Age=21)
    """
    print(type(kwargs))
    print(kwargs)

def display4(passenger_name, *baggage_tuple):
    """
    display4("Jack",12,8,5)
    display4("Chan",20,12)
    display4("Henry",23)
    """
    print("Passenger name:",passenger_name)
    total_wt=0
    for baggage_wt in baggage_tuple:
        total_wt+=baggage_wt
    print("Total baggage weight in kg:", total_wt)

'''This program is expected to display all the even numbers
between 1 and n (both inclusive)'''
i=1
n=10
while(i<=n):
    if(i%2==0):
        print(i)
    i+=1

baggage_count = 100
no_of_baggage_picked = 0
while baggage_count > 0:
    no_of_baggage_picked = 5
    baggage_count -= no_of_baggage_picked
    print("No. of baggage remaining:",baggage_count)


start = 1 
end = 20
step = 2 # step is exceptional the default valu of step is 1
for number in range(start,end,step):
    print("The current number is",number)
print("---------------------------")
for number in range(1,5):
    print("The current number is ",number)

print("----------------------------")

for number in range(1,7,2):
    print("The current number is ", number)
print("----------------------------")

for number in range(5,0,-1):
    print("The current number is ", number)
print("---------------------------")
start=1
end=6
for i in range(start, end):
    print("The data doesn't exiest for file ",i)
print("----------------------------")
def Number(start, end):
    for i in range(start,end):
        print("File no.",i)
Number(1,6)


# Python Program to Count words in a String using Dictionary
def freq(string,passedkey):
"""freq("Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go","little")"""

    #step1: A list variable is declared and initialized to an empty list.
    words = []

    #step2: Break the string into list of words
    words = string.split() # or string.lower().split()

    #step3: Declare a dictionary
    Dict = {}

    #step4: Use for loop to iterate words and values to the dictionary
    for key in words:
        if(key == passedkey):
            Dict[key] = words.count(key)   
    #step5: Print the dictionary
    print("Total Count:",Dict)

def display(num):
    message = ""
    """We initialize the message variable as an empty string.
Based on the value of num, the function checks:
If divisible by both 3 and 5, it sets the message to "Zoom".
If divisible only by 3, the message is set to "Zip".
If divisible only by 5, the message is set to "Zap".
If none of the conditions are met, the message is "Invalid".
Finally, it returns the message.
"""
    if num % 3 == 0 and num % 5 == 0:
        message = "Zoom"
    elif num % 3 == 0:
        message = "Zip"
    elif num % 5 == 0:
        message = "Zap"
    else:
        message = "Invalid"
    
    return message

# Provide different values for num and test your program
message = display(10)
print(message)  # Expected output: "Zip"
massage = display(15)
print(massage)  # Expected output: "Zoom"
message = display(25)
print(message)  # Expacted output: "Zap"
