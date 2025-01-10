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
