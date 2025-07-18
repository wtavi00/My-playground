import matplotlib .pyplot as plt
import numpy as np

def display1(flight_number, seating_capacity):
    print("Flight Number:", flight_number)
    print("Seating Capacity:", seating_capacity)

print("code-1: positional arguments")
display1("AI789",200)

#Uncomment and execute the below function call statement and observe the output
#display1(300,"BA123")


def display2(flight_number, seating_capacity):
    print("Flight Number:", flight_number)
    print("Seating Capacity:", seating_capacity)

print("\n")
print("code-2: keyword arguments")
display2(seating_capacity=250, flight_number="AI789")

def display3(flight_number, flight_make="Boeing", seating_capacity=150):
    print("Flight Number:", flight_number)
    print("Flight Make:", flight_make)
    print("Seating Capacity:", seating_capacity)

print("\n")
print("code-3: default arguments")
display3("AI789","Eagle")

#Uncomment and execute the below function call statements one by one and observe the output
#display3("BA234")
#display3("SI678","Qantas",200)


def display4(passenger_name, *baggage_tuple):
    print("Passenger name:",passenger_name)
    total_wt=0
    for baggage_wt in baggage_tuple:
        total_wt+=baggage_wt
    print("Total baggage weight in kg:", total_wt)

print("\n")
print("code-4: variable argument count")
display4("Jack",12,8,5)

#Uncomment and execute the below function call statements one by one and observe the output
#display4("Chan",20,12)
#display4("Henry",23)

print("\n")

def calculate_total_ticket_cost(no_of_adults, no_of_children):
    """The flight ticket rates for a round-trip (Mumbai->Dubai) were as follows: 
Rate per Adult: Rs. 37550.0 
Rate per Child: 1/3rd of the rate per adult 
Service Tax: 7% of the ticket amount (including all passengers) 
As it was a holiday season, the airline also offered 10% discount on the final ticket cost (after inclusion of the service tax).
Find and display the total ticket cost for a group which had adults and children.
>Test the program with different input values for number of adults and children"""
    
    adults=37550.0
    children= adults/3
    service_tax= 0.07
    discount= 0.10
    rate_of_adults= adults*no_of_adults
    rate_of_children= children*no_of_children
    total_cost= rate_of_adults+rate_of_children
    
    service= service_tax*total_cost
    total_with_tax=total_cost+service
    
    discount_cost=total_with_tax*discount
    total_with_discount= total_with_tax-discount_cost
    
    total_ticket_cost=total_with_discount

    return total_ticket_cost


#Provide different values for no_of_adults, no_of_children and test your program
total_ticket_cost=calculate_total_ticket_cost(5,2)
print("Total Ticket Cost:",total_ticket_cost)

print("\n")

# From there though code is to test a perticuler built in program (return)
#Code1
print("code-1")
def func1(a,b):
    return a+b

res=func1(5,10)
print("Value returned:",res)


#Code2:
print("------------------------------------")
print("code-2")
def func2():
    print("This code has nothing to return")
    return

func2()

#Code3:
print("------------------------------------")
print("code-3")
def func3():
    print("This code also has nothing to return and there is no return statement")

func3()

#Code 4:
print("------------------------------------")
print("code-4")
print("------------------------------------")

def func4(a,b):
    if(a>b):
        print("returns from if block")
        return a
    print("returns from outside if block")
    return b
print("1st invocation of code-4")
print("Value returned:",func4(10,5))
print("------------------------------------")
print("2nd invocation of code-4")
print("Value returned:",func4(2,3))
print("\n")
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

print("\n")

def find_sum_of_digits(number):
    """Write a Python program to find the sum of digits of a given number. E.g. Sum of number 123 will be 6
Note: Initialize the number with various values and test your program"""
    sum_of_digits=0     # Initialize the sum of digits to zero
    while number>0:     # Continue until the number is reduced to zero
        sum_of_digits+=number%10    # Add the last digit to the sum
        number//=10    # Remove the last digit from the number
    return sum_of_digits

#Provide different values for number and test your program
sum_of_digits=find_sum_of_digits(123)
print("Sum of digits:",sum_of_digits)
sum_of_digits=find_sum_of_digits(234)
print("The sum of digit you are looking for is:",sum_of_digits)

print("\n")

def find_product(num1,num2,num3):
    """Write a python program to find and display the product of three positive integer values based on the rule mentioned below:
It should display the product of the three values except when one of the integer value is 7. In that case, 7 should not be included in the product and the values to its left also should not be included.
If there is only one value to be considered, display that value itself. If no values can be included in the product, display -1."""
    # Create a list of the three integers
    num_list=[num1,num2,num3]
    # Cheak If 7 in the list
    if 7 in num_list:
        index_seven=num_list.index(7) # Finde the 7
        num_list=num_list[index_seven +1:]# Consider the values only to the right of 7
    # If there is no value left, returnt -1
    if not num_list:
        return -1
    product=1  # If there are values, calculate their product
    for val in num_list:
        product*=val
    return product

a=find_product(1,5,3)
print(a)
b=find_product(1,5,7)
print(b)

print("\n")

def form_triangle(num1,num2,num3):
    #Do not change the messages provided below
    success="Triangle can be formed"
    failure="Triangle can't be formed"

    if num1+num2>num3 and num1+num3>num2 and num2+num3>num1:
        return success
    else:
        return failure

#Provide different values for the variables, num1, num2, num3 and test your program
num1=3
num2=3
num3=5
print(form_triangle(num1, num2, num3))

print("\n")

def make_amount(rupees_to_make, no_of_five, no_of_one):
    # Setting a diffolt valu zero
    five_needed=0 
    one_needed=0 

    # Maximize the use of 5 rupee coins
    five_needed = min(rupees_to_make // 5, no_of_five)
    remaining_amount = rupees_to_make - (five_needed * 5)
    
    # Check if the remaining amount can be covered by 1 rupee coins
    if remaining_amount <= no_of_one:
        one_needed = remaining_amount
        print("No. of Five needed :", five_needed)
        print("No. of One needed  :", one_needed)
    else:
        print(-1)
        
make_amount(28, 8, 5)  # Expected Output: No. of Five needed : 5, No. of One needed : 3
make_amount(11, 2, 11) # Expected Output: No. of Five needed : 2, No. of One needed : 1
make_amount(19, 3, 3)  # Expected Output: -1
print("\n")

def calculate_bill_amount(food_type, quantity_ordered, distance_in_kms):
    bill_amount = 0
    
    # Define prices
    VEG_COMBO_PRICE = 120
    NON_VEG_COMBO_PRICE = 150
    
    # Validate inputs
    if (food_type != 'V' and food_type != 'N') or quantity_ordered < 1 or distance_in_kms <= 0:
        return -1  # Invalid inputs, return -1
    
    # Calculate base price based on food type
    if food_type == 'V':
        bill_amount = VEG_COMBO_PRICE * quantity_ordered
    elif food_type == 'N':
        bill_amount = NON_VEG_COMBO_PRICE * quantity_ordered
    
    # Calculate delivery charges based on distance
    if distance_in_kms > 3:
        if distance_in_kms <= 6:
            bill_amount += (distance_in_kms - 3) * 3  # Charge Rs. 3 for kms between 3 and 6
        else:
            bill_amount += (3 * 3)  # Charge Rs. 3 for kms from 4 to 6
            bill_amount += (distance_in_kms - 6) * 6  # Charge Rs. 6 for kms above 6
    
    return bill_amount
    print()
