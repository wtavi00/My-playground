# Creating a list for further function iteration
a_list = [2, 3, 44, 5, 56, 5, 4, 64, 35]

# Function to find the maximum element in a list
def find_max_in_list(some_list):
    max_element = some_list[0]  # Read the first element
    length = len(some_list)  # Count the length
    for i in range(1, length):  # Start loop from the second element
        if some_list[i] > max_element:  # Check for the maximum value
            max_element = some_list[i]  # Update max_element
    return max_element

z = find_max_in_list(a_list)
print(z)

# This is an alternate program using the built-in max function
def find_max(some_list):
    count = max(some_list)  # Python has a built-in function max() to get the max value from a list
    return count

x = find_max(a_list)  # Corrected variable name
print(x)

print("------------------------")

# Function with a regular for loop using the range function
def a_function():
    for i in range(3):  # This function will print a string 3 times starting from 0
        print("Serial No.", i)

a_function()

print("------------------------")

# Conditional check example
def will_work():
    if 10 > 5:
        print("Well, 10 is greater than 5")
    else:
        print("I don't know what to expect")

will_work()

print("------------------------")

# Defining a Customer class
class Customer:
    """This class has its own state and is separated from other states"""
    def __init__(self, cust_id, age):
        self.cust_id = cust_id
        self.age = age

c1 = Customer(100, 20)

def change(c2):
    c2.age = 21  # Updating the attribute of the passed object

change(c1)
print(c1.age)  # The age remains 20 because reassignment inside the function creates a new object

print("------------------------")

# Function documentation example
def doc_function():
    """This function does something that is well documented"""
    print("This is only for the document")

print(doc_function.__doc__)

another_fn = doc_function
print(another_fn.__doc__)

# Introduction function
def intro(name, city):
    """This is an introduction with name and city"""
    print("HELLO, My name is:", name)
    print("I work and live in", city)

intro("John Melan", "Dallas")

print("------------------------")

# Introduction function with school
def introduction(name, city, school):
    print("HELLO, My name is:", name)
    print("I live and work in:", city)
    print("And I am from:", school)

introduction("John Doe", "Miami", "Miami")
introduction(name="David", city="New York", school="New York")

print("------------------------")

# Square function
def square(x):
    """This function performs a mathematical equation"""
    print("The square of", x, "is", x * x)

square(3)
square(10012)
num = 35
square(num)

print("------------------------")

# Savings calculation
def savings(a, b):
    print("The total savings is:", a - b)

savings(30, 5)

print("------------------------")

# Savings function with global variables
salary = 1000
expense = 300

def my_savings(salary, expense):
    print("Total:", salary - expense)

my_savings(salary, expense)

print("------------------------")

# Function that prints a string multiple times
def many_times(string, times):
    """ This program will print a string a certain number of times.
        Parameters (both required):
        string (str): The string to be printed
        times (int): The number of times the string should be printed
        No return value
    """
    for i in range(times):
        print(string)

many_times("Hello", 3)
print(many_times.__doc__)

print("------------------------")

# Function to find the higher number
def higher_number(a, b):
    # Checking which number is higher
    if a > b:
        print("The higher number is", a)
    elif a < b:
        print("The higher number is", b)
    else:
        print("Both numbers are equal")

higher_number(20, 23)
higher_number(21, 21)

print("---------------------")
