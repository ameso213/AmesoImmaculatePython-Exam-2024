#i)

def calculate_circle_area(radius):
    # (Assuming that π is ≈ 3.14)
    pi = 3.14
    # using the formula 
    area = pi * (radius ** 2)
    return area

# Test the function with a radius of 4
radius = 4
area = calculate_circle_area(radius)
area



#ii)

# Given list of integers
numbers = [4, 7, 2, 9, 12, 15]

# Initialize the sum of odd numbers
sum_of_all_odds_numbers = 0

# Loop through each number in the list
for number in numbers:
    # Check if the number is odd
    if number % 2 != 0:
        sum_of_all_odds_numbers += number  # Add the odd number to the sum

# Print the result
print(f"The sum of all odd numbers is: {sum_of_all_odds_numbers}")



#iii)

def calculate_operations(num1, num2):
    
    sum_result = num1 + num2
    difference_result = num1 - num2
    product_result = num1 * num2
    
    
    if num2 != 0:
        quotient_result = num1 / num2
    else:
        quotient_result = "undefined"  # Avoid division by zero
    
    return sum_result, difference_result, product_result, quotient_result


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


sum_result, difference_result, product_result, quotient_result = calculate_operations(num1, num2)

# Print the results
print(f"Sum: {sum_result}")
print(f"Difference: {difference_result}")
print(f"Product: {product_result}")
print(f"Quotient: {quotient_result}")




#v)

# Given dictionary
student_info = {"name": "Alice", "age": 20, "grade": "A"}

# Update the age to 26
student_info["age"] = 26

# Add a new key-value pair for city
student_info["city"] = "Kampala"

# Print the updated dictionary
print(student_info)
