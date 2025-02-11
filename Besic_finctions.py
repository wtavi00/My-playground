def a_function():
    # Regular for loop using range function
    for i in range(3):
        print("Serial No.", i)

a_function()

def will_work():
    # Conditional check (if statement)
    print("This indentation is all right")
    if 10 > 5:
        print("Well, 10 is greater than 5")

will_work()

def doc_function():
    """This function does something that is well documented"""
    print("This is only for the document")

print(doc_function.__doc__)
another_fn = doc_function
print(another_fn.__doc__)

def intro(name, city):
    """Introduction function with name and city"""
    print("HELLO, My name is:", name)
    print("I work and live in", city)

intro("Devide", "New York")

def my_intro():
    print("Hello, this is William")
    print("I live in Brasil")

my_intro()

def introduction(name, city, school):
    print("HELLO, My name is:", name)
    print("I live and work in:", city)
    print("And I am from:", school)

introduction("Devid Melan", "London", "Harverd")
introduction(name="Jhone", city="Miami", school="Miami")

def square(x):
    print("The square of", x, "is", x * x)

square(3)
square(10012)
num = 35
square(num)

def savings(a, b):
    print("The total savings is:", a - b)

savings(30, 5)

salary = 1000
expense = 300

def my_savings(salary, expense):
    print("Total savings:", salary - expense)

my_savings(salary, expense)

def many_times(string, times):
    """Repeats a given string a certain number of times"""
    for i in range(times):
        print(string)

many_times("Hello", 3)
print(many_times.__doc__)

def higher_number(a, b):
    # Checking which number is higher
    if a > b:
        print("The higher number is", a)
    else:
        print("The higher number is", b)

higher_number(20, 23)
higher_number(21, 21)

def multiply(num1, num2, num3):
    print("Multiplication of these three numbers is", num1 * num2 * num3)

multiply(2, 4, 5)

def positive_negative_zero(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

p = positive_negative_zero(2)
n = positive_negative_zero(-1)
o = positive_negative_zero(0)
print(p, n, o)

def find_max_in_list(some_list):
    if not some_list:
        print("Zero element list")
        return None
    return max(some_list)

a_list = [43, 4, 56, 8, 89321, 3, 34, 52, 62, 564, 673, 54, 65, 56545]
empty_list = []
print(find_max_in_list(a_list))
print(find_max_in_list(empty_list))

def create_dictionary_intro(name, age, job):
    return {"Name": name, "Age": age, "Job": job}

i = create_dictionary_intro(name="Ravi", age=21, job="Student")
print(i)

def generate_list(name, num_elements):
    return [name for _ in range(num_elements)]

print(generate_list("Generate Sequense No.", 3))

def calculator(a, b, operator):
    if operator == "add":
        return a + b
    elif operator == "sub":
        return a - b
    elif operator == "mul":
        return a * b
    elif operator == "div":
        return a / b
    else:
        return "Invalid operator"

print(calculator(5, 3, "add"))
print(calculator(5, 4, "sub"))
print(calculator(5, 4, "mul"))
print(calculator(10, 5, "div"))
print(calculator(10, 2, "dev"))

def student_details(name, school, math, physics, chemistry, biology, enrolled=False):
    total = math + physics + chemistry + biology
    print("Name:", name)
    print("School:", school, "Enrolled:", enrolled)
    print("Total Score:", total)

student_details("Devid", "MGHS", 90, 34, 56, 89, enrolled="Yes")
student_details("Jhon", "MGHS", 90, 34, 43, 89)

def display(flight_number, seating_capacity=150):
    print("Flight Number:", flight_number)
    print("Seating Capacity:", seating_capacity)

display("AI789", 200)
display("BA234")
