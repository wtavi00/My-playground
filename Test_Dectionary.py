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

print("-------------------------------------------------")
print("code-2: keyword arguments")
display2(seating_capacity=250, flight_number="AI789")

def display3(flight_number, flight_make="Boeing", seating_capacity=150):
    print("Flight Number:", flight_number)
    print("Flight Make:", flight_make)
    print("Seating Capacity:", seating_capacity)

print("-------------------------------------------------")
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

print("-------------------------------------------------")
print("code-4: variable argument count")
display4("Jack",12,8,5)
#Uncomment and execute the below function call statements one by one and observe the output
#display4("Chan",20,12)
#display4("Henry",23)

print("------------------------------------")

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

print("------------------------------------")

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
print("------------------------")
def infinite_loop():  #This is an infinite loops, always ensure that loop will terminate in finite number
    counter=5
    while counter >=5:
        print(counter)
        counter=counter+1

print("------------------------")
counter=2
while counter <=3:
    print(counter)
    counter +=1
print("-----------------------")
num_list =[1,2,3,4,5]
for num in num_list:
    print(num, end=" ")
print("------------------------")

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

print("-------------------------")

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
print("------------------------")
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

print("------------------------")
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

# Test the function with different values
make_amount(28, 8, 5)  # Expected Output: No. of Five needed : 5, No. of One needed : 3
make_amount(11, 2, 11) # Expected Output: No. of Five needed : 2, No. of One needed : 1
make_amount(19, 3, 3)  # Expected Output: -1

print("------------------------------")
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

# Provide different values for food_type, quantity_ordered, and distance_in_kms to test your program
bill_amount = calculate_bill_amount("N", 2, 7)
print(bill_amount)

print("---------------------")
def calculate_loan(account_number, salary, account_balance, loan_type, loan_amount_expected, customer_emi_expected):
    eligible_loan_amount = 0
    bank_emi_expected = 0

    # Check if account number is valid
    if len(str(account_number)) != 4 or str(account_number)[0] != '1':
        print("Invalid account number")
        return

    # Check if account balance is at least 1 lakh
    if account_balance < 100000:
        print("Insufficient account balance")
        return

    # Define loan eligibility based on salary and loan type
    if loan_type == "Car" and salary > 25000:
        eligible_loan_amount = 500000
        bank_emi_expected = 36
    elif loan_type == "House" and salary > 50000:
        eligible_loan_amount = 6000000
        bank_emi_expected = 60
    elif loan_type == "Business" and salary > 75000:
        eligible_loan_amount = 7500000
        bank_emi_expected = 84
    else:
        print("Invalid loan type or salary")
        return

    # Check if requested loan amount and EMI are within the eligible limits
    if loan_amount_expected > eligible_loan_amount or customer_emi_expected > bank_emi_expected:
        print("The customer is not eligible for the loan")
        return

    # Display eligible information in case of success
    print("Account number:", account_number)
    print("The customer can avail the amount of Rs.", eligible_loan_amount)
    print("Eligible EMIs :", bank_emi_expected)
    print("Requested loan amount:", loan_amount_expected)
    print("Requested EMI's:", customer_emi_expected)

# Test the function with a sample input
calculate_loan(1001, 40000, 250000, "Car", 300000, 30)

print("---------------------")

def get_count(num_list):
    """Given a list of integer values. Write a python program to check whether it contains same number in adjacent position. Display the count of such adjacent occurrences"""
    count = 0
    for i in range(len(num_list) - 1):
        if num_list[i] == num_list[i + 1]:
            count += 1
    return count

# Provide different values in the list and test your program
num_list = [1, 1, 5, 100, -20, -20, 6, 0, 0]
print(get_count(num_list))
num_list=[10,20,30,40,30,20]
print(get_count(num_list))
num_list=[1,2,2,3,4,4,4,10]
print(get_count(num_list))

print("---------------------")
def solve(heads, legs):
    """Write a python program to solve a classic ancient Chinese puzzle.
    We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?"""
    error_msg = "No solution"
    chicken_count = 0
    rabbit_count = 0

    # Calculate the number of rabbits using the formula derived from the equations
    rabbit_count = (legs - 2 * heads) / 2
    chicken_count = heads - rabbit_count

    # Check if we have valid integer values for chickens and rabbits
    if rabbit_count.is_integer() and chicken_count.is_integer() and rabbit_count >= 0 and chicken_count >= 0:
        chicken_count = int(chicken_count)
        rabbit_count = int(rabbit_count)
        print(chicken_count, rabbit_count)
    else:
        print(error_msg)

# Provide different values for heads and legs and test your program
solve(38, 131)

print("---------------------")
def find_max(num1, num2):
    """Write a python program which finds the maximum number from num1 to num2 (num2 inclusive) based on the following rules.
1. Always num1 should be less than num2
2. Consider each number from num1 to num2 (num2 inclusive). Populate the number into a list, if the below conditions are satisfied
      a. Sum of the digits of the number is a multiple of 3
      b. Number has only two digits
      c. Number is a multiple of 5
3. Display the maximum element from the list
In case of any invalid data or if the list is empty, display -1."""

    # Initialize max_num as -1, to return in case of invalid data or empty list
    max_num = -1

    # Check if num1 is less than num2
    if num1 >= num2:
        return max_num

    # Loop through numbers from num1 to num2 inclusive
    for num in range(num1, num2 + 1):
        # Check conditions
        if (10 <= num <= 99) and (sum(int(digit) for digit in str(num)) % 3 == 0) and (num % 5 == 0):
            max_num = max(max_num, num)

    return max_num

# Test with provided values
max_num = find_max(10, 15)
print(max_num)

print("---------------------")

def generate_ticket(airline, source, destination, no_of_passengers):
    ticket_number_list = []
    src = source[:3].upper()
    dest = destination[:3].upper()
    start_number = 101

    for i in range(no_of_passengers):
        ticket_number = f"{airline}:{src}:{dest}:{start_number + i}"
        ticket_number_list.append(ticket_number)

    # Return the last five tickets, or all if there are fewer than five passengers
    return ticket_number_list[-5:]

# Provide different values for airline, source, destination, no_of_passengers and test the program
print(generate_ticket("AI", "Bangalore", "London", 7))
print(generate_ticket("AI","Bangalore","London",10))
print(generate_ticket("BA", "Australia","France", 2))

print("---------------------")

row1 = (101,"Dallas",3.5)
row2 = (102,"Atlanta",5.6)
row3 = (103,"Tokyo",9.8)
table = [row1,row2,row3]
print(table[0])
print(table[1])
print(table[2])

print("---------------------")

def count_names(name_list):
    """Write a python program which displays the count of the names that matches a given pattern from a list of names provided.
Consider the pattern characters to be:
1. "_ at" where "_" can be one occurrence of any character
2. "%at%" where "%" can have zero or any number of occurrences of a character"""
    count1 = 0
    count2 = 0
    
    # Pattern "_at" where "_" can be any single character
    for name in name_list:
        if len(name) == 3 and name.endswith("at"):
            count1 += 1
            
    # Pattern "%at%" where "%" can be any number of characters including zero
    for name in name_list:
        if "at" in name:
            count2 += 1
            
    # Use the below given print statements to display the output
    print("_at -> ", count1)
    print("%at% -> ", count2)

# Provide different names in the list and test your program
name_list = ["Hat", "Cat", "Rabbit", "Matter"]
count_names(name_list)

print("---------------------")

def find_leap_years(given_year):
    list_of_leap_years=[]
    year = given_year

    while len(list_of_leap_years)< 15:
        if (year % 4== 0 and year %100!=0) or (year % 400 == 0):
            list_of_leap_years.append(year)
        year += 1
    return list_of_leap_years

list_of_leap_years = find_leap_years(2000)
print(list_of_leap_years)

print("---------------------")

def calculate_bill_amount(gems_list, price_list, reqd_gems, reqd_quantity):
    bill_amount = 0

    # Dictionary to map gems to their prices
    gem_prices = dict(zip(gems_list, price_list))

    # Calculate the bill amount
    for gem, quantity in zip(reqd_gems, reqd_quantity):
        if gem in gem_prices:
            bill_amount += gem_prices[gem] * quantity
        else:
            # If a gem is not available, return -1
            return -1

    # Apply discount if bill amount is greater than 30000
    if bill_amount > 30000:
        bill_amount *= 0.95  # Applying 5% discount

    return bill_amount

# List of gems available in the store
gems_list = ["Emerald", "Ivory", "Jasper", "Ruby", "Garnet"]

# Price of gems available in the store. gems_list and price_list have one-to-one correspondence
price_list = [1760, 2119, 1599, 3920, 3999]

# List of gems required by the customer
reqd_gems = ["Ivory", "Emerald", "Garnet"]

# Quantity of gems required by the customer. reqd_gems and reqd_quantity have one-to-one correspondence
reqd_quantity = [3, 10, 12]

# Calculate and print the bill amount
bill_amount = calculate_bill_amount(gems_list, price_list, reqd_gems, reqd_quantity)
print(bill_amount)

print("---------------------")

def create_largest_number(number_list):
    # Convert numbers to strings for concatenation
    number_list = list(map(str, number_list))
    
    # Sort numbers based on the custom key
    # The key is based on comparing concatenated values in reverse order
    number_list.sort(key=lambda x: x * 2, reverse=True)
    
    # Join sorted numbers to form the largest number
    largest_number = ''.join(number_list)
    return int(largest_number)  # Convert back to integer for final result

# Sample input and function call
number_list = [23, 34, 55]
largest_number = create_largest_number(number_list)
print(largest_number)  # Output: 553423
number_list = [23, 45, 67]
largest_number = create_largest_number(number_list)
print(largest_number)  # Output: 674523

print("---------------------")

def check_palindrome(word):
    # Compare the string with its reverse
    return word == word[::-1]

# Testing the function with the word "malayalam"
status = check_palindrome("malayalam")
if status:
    print("Word is a palindrome")
else:
    print("Word is not a palindrome")

print("---------------------")

def encode(message):
    # Initialize an empty string to store the encoded result
    encoded = ""
    n = len(message)

    # Start the index at 0
    i = 0
    while i < n:
        # Count the number of repetitions of the current character
        count = 1
        while i + 1 < n and message[i] == message[i + 1]:
            count += 1
            i += 1

        # Append the count and character to the encoded string
        encoded += str(count) + message[i]
        i += 1

    return encoded

# Provide different values for message and test your program
print(encode("AAAABBBBCCCCCCCC"))  # Expected Output: 4A4B8C
print(encode("AABCCA"))            # Expected Output: 2A1B2C1A
print(encode("ABBBBCCCCCCCCAB"))   # Expected Output: 1A4B8C1A1B

print("---------------------")

# Initialize data
child_id = (10, 20, 30, 40, 50)
chocolates_received = [12, 5, 3, 4, 6]

def calculate_total_chocolates():
    # Calculate and return the total number of chocolates
    return sum(chocolates_received)

def reward_child(child_id_rewarded, extra_chocolates):
    # Check if the number of extra chocolates is less than 1
    if extra_chocolates < 1:
        print("Extra chocolates is less than 1")
        return
    
    # Check if the child_id_rewarded exists in child_id
    if child_id_rewarded not in child_id:
        print("Child id is invalid")
        return
    
    # Add the extra chocolates to the corresponding child
    index = child_id.index(child_id_rewarded)
    chocolates_received[index] += extra_chocolates
    
    # Print the updated chocolates_received list
    print(chocolates_received)

# Test the functions
print(calculate_total_chocolates())  # Output the total number of chocolates
reward_child(20, 2)  # Reward child with ID 20 with 2 extra chocolates

print("---------------------")

def translate(bilingual_dict, english_words_list):
    """Represent a small bilingual (English-Swedish) glossary given below as a Python dictionary
{"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"} 
and use it to translate your Christmas wishes from English into Swedish.
That is, write a python function translate() that accepts the bilingual dictionary and a list of English words (your Christmas wish) and returns a list of equivalent Swedish words"""
    # Translate each word in the English words list using the bilingual dictionary
    swedish_words_list = [bilingual_dict.get(word.lower(), word) for word in english_words_list]
    return swedish_words_list


bilingual_dict = {
    "merry": "god",
    "christmas": "jul",
    "and": "och",
    "happy": "gott",
    "new": "nytt",
    "year": "ar"  # Adjusted to match your initial input
}

english_words_list = ["merry", "christmas"]

print("The bilingual dict is:", bilingual_dict)
print("The english words are:", english_words_list)

swedish_words_list = translate(bilingual_dict, english_words_list)
print("The equivalent swedish words are:", swedish_words_list)

print("---------------------")

def find_number_of_combination(number_of_flavours):
    # Each topping can either be included or excluded
    total_combination = 2 ** number_of_flavours
    return total_combination

# Provide different values for number_of_flavours and test your program
number_of_combination = find_number_of_combination(6)
print(number_of_combination)  # Output: 64

print("---------------------")

def find_common_characters(msg1, msg2):
    # Remove spaces and convert strings to lowercase for accurate comparison
    msg1_set = set(msg1)
    msg2_set = set(msg2)
    
    # Find common characters
    common_chars = msg1_set & msg2_set
    
    # Check if there are any common characters
    if common_chars:
        return ''.join(sorted(common_chars))  # Return sorted common characters as a string
    else:
        return -1  # Return -1 if no common characters

# Provide different values for msg1, msg2 and test your program
msg1 = "I like Python"
msg2 = "Java is a very popular language"
common_characters = find_common_characters(msg1, msg2)
print(common_characters)
msg1 = "Python"
msg2 = "python"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)

print("---------------------")

def find_common_characters(msg1, msg2):
    """Write a python program to display all the common characters between two strings. Return -1 if there are no matching characters.
Note: Ignore blank spaces if there are any. Perform case sensitive string comparison wherever necessary."""

    # Use a set to find common characters
    common_chars = set(msg1) & set(msg2)
    
    # Convert the set to a sorted list and then to a string
    if common_chars:
        return ''.join(sorted(common_chars))
    else:
        return -1

# Test the function
msg1 = "Python"
msg2 = "python"
common_characters = find_common_characters(msg1, msg2)
print(common_characters) 

print("---------------------")

def encrypt_sentence(sentence):
    def is_vowel(ch):
        """Check if a character is a vowel."""
        return ch.lower() in 'aeiou'

    def process_word(word, position):
        """Process a word based on its position (odd or even)."""
        if position % 2 == 1:  # Odd position
            return word[::-1]
        else:  # Even position
            consonants = ''.join([ch for ch in word if not is_vowel(ch)])
            vowels = ''.join([ch for ch in word if is_vowel(ch)])
            return consonants + vowels

    # Split the sentence into words
    words = sentence.split()

    # Process each word based on its position
    encrypted_words = [process_word(word, i + 1) for i, word in enumerate(words)]

    # Join the processed words to form the encrypted sentence
    return ' '.join(encrypted_words)

# Test the function
sentence = "The sun rises in the east"
encrypted_sentence = encrypt_sentence(sentence)
print(encrypted_sentence)

print("---------------------")

# Duplicate and test program
def rearrange_word(word):
    # Initialize empty strings for consonants and vowels
    consonants = ""
    vowels = ""
    
    # Define a set of vowels for easy checking
    vowel_set = set("aeiouAEIOU")
    
    # Separate consonants and vowels while maintaining their order
    for char in word:
        if char in vowel_set:
            vowels += char
        else:
            consonants += char
            
    # Return the concatenation of consonants followed by vowels
    return consonants + vowels

def encrypt_message(message):
    # Split the message into a list of words
    words = message.split()
    
    # Initialize an empty list to store the processed words
    encrypted_words = []
    
    # Iterate over the list of words with their indices
    for index, word in enumerate(words):
        # Check if the position (1-based index) is odd or even
        if (index + 1) % 2 == 1:  # Odd position
            encrypted_words.append(word[::-1])  # Reverse the word
        else:  # Even position
            encrypted_words.append(rearrange_word(word))  # Rearrange the word
    
    # Join the words in encrypted_words with a single space to form the final encrypted message
    return ' '.join(encrypted_words)

# Example usage
if __name__ == "__main__":
    message = "the sun rises in the east"
    encrypted_message = encrypt_message(message)
    print(encrypted_message)

print("---------------------")

def find_correct(word_dict):
    # Initialize counters for the three categories
    correct_count = 0
    almost_correct_count = 0
    wrong_count = 0

    for correct_word, contestant_word in word_dict.items():
        # Check if lengths match
        if len(correct_word) != len(contestant_word):
            wrong_count += 1
        else:
            # Count the number of differing characters
            differences = sum(1 for c1, c2 in zip(correct_word, contestant_word) if c1 != c2)
            if differences == 0:
                correct_count += 1
            elif differences <= 2:
                almost_correct_count += 1
            else:
                wrong_count += 1

    # Return the counts as a list
    return [correct_count, almost_correct_count, wrong_count]

# Example usage
word_dict = {
    "THEIR": "THEIR",
    "BUSINESS": "BISINESS",
    "WINDOWS": "WINDMILL",
    "WERE": "WEAR",
    "SAMPLE": "SAMPLE"
}
print(find_correct(word_dict))

print("---------------------")

def max_visited_speciality(patient_medical_speciality_list, medical_speciality):
    """Care hospital wants to know the medical speciality visited by the maximum number of patients. Assume that the patient id of the patient along with the medical speciality visited by the patient is stored in a list. The details of the medical specialities are stored in a dictionary as follows:
{
"P":"Pediatrics",
"O":"Orthopedics",
"E":"ENT
} 

Write a function to find the medical speciality visited by the maximum number of patients and return the name of the speciality.

Note: 
Assume that there is always only one medical speciality which is visited by maximum number of patients.
Perform case sensitive string comparison wherever necessary."""
    # Dictionary to store counts of visits for each speciality code
    speciality_count = {}
    
    # Iterate over the list to count the visits for each speciality
    for i in range(1, len(patient_medical_speciality_list), 2):
        speciality_code = patient_medical_speciality_list[i]
        if speciality_code in speciality_count:
            speciality_count[speciality_code] += 1
        else:
            speciality_count[speciality_code] = 1
    
    # Find the speciality code with the maximum visits
    max_speciality_code = max(speciality_count, key=speciality_count.get)
    
    # Return the name of the speciality using the medical_speciality dictionary
    return medical_speciality[max_speciality_code]

# Provide different values in the list and test your program
patient_medical_speciality_list = [301, 'P', 302, 'P', 305, 'P', 401, 'E', 656, 'E']
medical_speciality = {"P": "Pediatrics", "O": "Orthopedics", "E": "ENT"}
speciality = max_visited_speciality(patient_medical_speciality_list, medical_speciality)
print(speciality)

print("---------------------")

def sms_encoding(data):
    # Helper function to determine if a character is a vowel
    def is_vowel(char):
        return char.lower() in 'aeiou'

    # Split the sentence into words
    words = data.split()

    # Encode each word based on the rules
    encoded_words = []
    for word in words:
        # Check if the word has any consonants
        if any(not is_vowel(char) for char in word if char.isalpha()):
            # Retain only consonants
            encoded_word = ''.join(char for char in word if not is_vowel(char))
        else:
            # Retain the word as is if it has only vowels
            encoded_word = word
        encoded_words.append(encoded_word)

    # Join the encoded words with spaces
    return ' '.join(encoded_words)

# Example usage
data = "I love Python"
print(sms_encoding(data))  # Output: "I lv Pythn"

print("---------------------")

def max_frequency_word_counter(data):
    word = ""
    frequency = 0

    # Start writing your code here
    # Convert the text to lowercase to perform case-insensitive comparisons
    data = data.lower()
    # Split the text into individual words
    words = data.split()
    # Create a dictionary to store word frequencies
    word_counts = {}

    # Count the frequency of each word
    for w in words:
        word_counts[w] = word_counts.get(w, 0) + 1

    # Find the word with the largest frequency and the longest length in case of ties
    for w, count in word_counts.items():
        if count > frequency or (count == frequency and len(w) > len(word)):
            word = w
            frequency = count

    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work
    print(word, frequency)


# Provide different values for data and test your program
data = "Work like you do not need money, love like you have never been hurt, and dance like no one is watching"
max_frequency_word_counter(data)
data = "Courage is not the absence of fear but rather the judgement that something else is more important than fear"
max_frequency_word_counter(data)

print("---------------------")

def factorial(number):
    """Returns the factorial of a given number."""
    if number == 0 or number == 1:
        return 1
    result = 1
    for i in range(2, number + 1):
        result *= i
    return result


def find_strong_numbers(num_list):
    """Returns a list of Strong numbers from the given list."""
    strong_numbers = []
    for num in num_list:
        digit_factorial_sum = sum(factorial(int(digit)) for digit in str(num))
        if digit_factorial_sum == num:
            strong_numbers.append(num)
    return strong_numbers


# Example usage
num_list = [145, 375, 100, 2, 10]
strong_num_list = find_strong_numbers(num_list)
print(strong_num_list)

print("---------------------")

def find_pairs_of_numbers(num_list, n):
    """Write a python function, find_pairs_of_numbers() which accepts a list of positive integers with no repetitions and returns count of pairs of numbers in the list that adds up to n. The function should return 0, if no such pairs are found in the list."""
    # Initialize a set to store seen numbers
    seen = set()
    # Initialize a counter for the pairs
    count = 0
    
    # Iterate through the numbers in the list
    for num in num_list:
        # Calculate the complement
        complement = n - num
        # Check if the complement is in the set
        if complement in seen:
            count += 1
        # Add the current number to the set
        seen.add(num)
    
    return count

# Test the function
num_list = [1, 2, 4, 5, 6]
n = 6
print(find_pairs_of_numbers(num_list, n))

print("---------------------")

def create_largest_number(number_list):
    """Write a python function, create_largest_number(), which accepts a list of numbers and returns the largest number possible by concatenating the list of numbers. 
Note: Assume that all the numbers are two digit numbers."""
    number_list =list(map(str, number_list))
    
    number_list.sort(key=lambda x:x*2, reverse=True)
    largest_number = ''.join(number_list)
    return int(largest_number)

number_list=[23,45,67]
largest_number=create_largest_number(number_list)
print(largest_number)
number_list=[23,34,55]
largest_number=create_largest_number(number_list)
print(largest_number)

print("---------------------")

# Global variable
list_of_marks = (12, 18, 25, 24, 2, 5, 18, 20, 20, 21)
"""A teacher is in the process of generating few reports based on the marks scored by the students of her class in a project based assessment.
Assume that the marks of her 10 students are available in a tuple. The marks are out of 25.

Write a python program to implement the following functions:
1. find_more_than_average(): Find and return the percentage of students who have scored more than the average mark of the class.
2. generate_frequency(): Find how many students have scored the same marks. For example, how many have scored 0, how many have scored 1, how many have scored 3….how many have scored 25. The result should be populated in a list and returned.
3. sort_marks(): Sort the marks in the increasing order from 0 to 25. The sorted values should be populated in a list and returned"""

def find_more_than_average():
    """
    Calculate the percentage of students who scored more than the average marks.
    
    :return: percentage of students who scored more than the average
    """
    average = sum(list_of_marks) / len(list_of_marks)
    count = sum(1 for mark in list_of_marks if mark > average)
    percentage = (count / len(list_of_marks)) * 100
    return percentage

def sort_marks():
    """
    Sort the marks in ascending order.
    
    :return: sorted list of marks
    """
    return sorted(list_of_marks)

def generate_frequency():
    """
    Generate the frequency of marks scored by students.
    
    :return: list containing frequency of marks from 0 to 25
    """
    frequency = [0] * 26  # Initialize a list with 26 zeros (for marks 0 to 25)
    for mark in list_of_marks:
        frequency[mark] += 1
    return frequency

# Test the functions
print(find_more_than_average())  # Output the percentage of students scoring above the average
print(generate_frequency())      # Output the frequency list
print(sort_marks())              # Output the sorted list of marks

print("---------------------")

 # Global variables
child_id = (10, 20, 30, 40, 50)
chocolates_received = [12, 5, 3, 4, 6]
"""A teacher is conducting a camp for a group of five children. Based on their performance and behavior during the camp, the teacher rewards them with chocolates.
Write a Python function to

1. Find the total number of chocolates received by all the children put together.
Assume that each child is identified by an id and it is stored in a tuple and the number of chocolates given to each child is stored in a list.
2. The teacher also rewards a child with few extra chocolates for his/her best conduct during the camp.

If the number of extra chocolates is less than 1, an error message "Extra chocolates is less than 1", should be displayed.

If the given child Id is invalid, an error message "Child id is invalid" should be displayed. Otherwise, the extra chocolates provided for the child must be added to his/her existing number of chocolates and display the list containing the total number of chocolates received by each child."""

def calculate_total_chocolates():
    """
    Calculate the total number of chocolates received by all children.
    """
    return sum(chocolates_received)

def reward_child(child_id_rewarded, extra_chocolates):
    """
    Reward extra chocolates to a child based on their ID.
    """
    if extra_chocolates < 1:
        print("Extra chocolates is less than 1")
        return

    if child_id_rewarded not in child_id:
        print("Child id is invalid")
        return

    # Find the index of the child in the child_id tuple
    index = child_id.index(child_id_rewarded)

    # Add the extra chocolates to the existing count
    chocolates_received[index] += extra_chocolates

    # Print the updated chocolates_received list
    print(chocolates_received)

# Test the functions
print(calculate_total_chocolates())  # Output: Total chocolates

# Test rewarding a child
reward_child(20, 2)  # Add 2 chocolates to the child with ID 20
reward_child(60, 2)  # Invalid child ID
reward_child(30, 0)  # Invalid extra chocolates

print("---------------------")

def find_ten_substring(num_str):
    """
    Finds all substrings of a number (represented as a string) that sum up to 10.
    
    :param num_str: String representing the number
    :return: List of 10-substrings
    """
    try:
        result_list = []
        
        # Iterate through each starting index of the substring
        for i in range(len(num_str)):
            current_sum = 0
            substring = ""
            
            # Expand the substring from the current starting index
            for j in range(i, len(num_str)):
                digit = int(num_str[j])  # Convert character to integer
                current_sum += digit
                substring += num_str[j]
                
                if current_sum == 10:
                    result_list.append(substring)
                    break  # Stop adding digits once we reach a sum of 10
                elif current_sum > 10:
                    break  # Stop adding digits if the sum exceeds 10
        
        return result_list
    except ValueError:
        print("Error: The input string contains non-numeric characters.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

# Test the function
num_str = "2825302"
print("The number is:", num_str)
result_list = find_ten_substring(num_str)
print(result_list)

print("---------------------")

import math

def find_smallest_number(n):
    """
    Finds the smallest number having exactly n divisors.
    
    Parameters:
        n (int): Number of divisors.

    Returns:
        int: Smallest number having exactly n divisors.
    """
    try:
        # Input validation
        if not isinstance(n, int):
            raise ValueError("Input must be an integer.")
        if n <= 0:
            raise ValueError("Input must be a positive integer.")
        
        # Helper function to count divisors of a number
        def count_divisors(num):
            count = 0
            for i in range(1, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    count += 2 if i != num // i else 1
            return count

        # Finding the smallest number with exactly n divisors
        number = 1
        while True:
            if count_divisors(number) == n:
                return number
            number += 1

    except ValueError as ve:
        return f"Error: {ve}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

# Test the function
num = 16
print("The number of divisors:", num)
result = find_smallest_number(num)
print("The smallest number having", num, "divisors:", result)

print("---------------------")

class Vehicle:
    """A vehicle is identified by its mileage (in kms per litre) and fuel left (in litres) in the vehicle. From the fuel left, 5 litres will always be considered as reserve fuel. At any point of time, the driver of the vehicle may want to know:

the maximum distance that can be covered without using the reserve fuel
how many kms he/she has already travelled based on the initial fuel the vehicle had
Identify the class name and attributes so as to represent a vehicle from the information given.

__init__()
Vehicle
Car
identify_disctance_that_can_be_travelled()
mileage
fuel_left
identify_distance_travelled(initial_fuel)

Write a Python program to implement the class chosen with its attributes and methods based on the requirements given below:
identify_distance_that_can_be_travelled(): Return the distance that can be travelled by the vehicle without using the reserve fuel. If the fuel left is less than or equal to reserve fuel, the method should return 0.
identify_distance_travelled(initial_fuel): Return the distance so far travelled by the vehicle based on the initial fuel,fuel left and mileage.
Assume that initial fuel is always greater than fuel left.
Represent a vehicle and test your program by initializing the instance variables and invoking the appropriate methods."""
    def __init__(self, mileage, fuel_left):
        self.mileage = mileage  # in km per litre
        self.fuel_left = fuel_left  # in litres

    def identify_distance_that_can_be_travelled(self):
        # Reserve fuel is 5 litres, so we can only use (fuel_left - 5) for travelling
        reserve_fuel = 5
        if self.fuel_left <= reserve_fuel:
            return 0
        return (self.fuel_left - reserve_fuel) * self.mileage

    def identify_distance_travelled(self, initial_fuel):
        # Distance travelled is based on the difference between initial and current fuel levels
        distance_travelled = (initial_fuel - self.fuel_left) * self.mileage
        return distance_travelled

# Testing the program
vehicle = Vehicle(mileage=15, fuel_left=10)

initial_fuel = 20  # Example initial fuel in litres

# Find the maximum distance the vehicle can travel without using reserve fuel
max_distance = vehicle.identify_distance_that_can_be_travelled()
print(f"Maximum distance that can be travelled without using reserve fuel: {max_distance} km")

# Find the distance travelled based on the initial fuel
distance_travelled = vehicle.identify_distance_travelled(initial_fuel)
print(f"Distance already travelled: {distance_travelled} km")
