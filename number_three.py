# Ask the user for their age
age = int(input("Please enter your age: "))

# Check if the age is greater than or equal to 18
if age >= 18:
    print("You are eligible")
else:
    print("You are not eligible")


#ii)

def grade_students(mark):
    # Check the range of the mark and return the corresponding grade
    if mark >= 90:
        return 'A'
    elif 80 <= mark < 90:
        return 'B'
    elif 70 <= mark < 80:
        return 'C'
    elif 60 <= mark < 70:
        return 'D'
    else:
        return 'F'

mark = int(input("Enter the student's mark: "))
grade = grade_students(mark)
print(f"The student's grade is: {grade}")



#iii)

def grade_students(mark):
    # Check the range of the mark and return the corresponding grade
    if mark >= 90:
        return 'A'
    elif 80 <= mark < 90:
        return 'B'
    elif 70 <= mark < 80:
        return 'C'
    elif 60 <= mark < 70:
        return 'D'
    else:
        return 'F'

# Test with the mark of 85
mark = 85 
grade = grade_students(mark)
print(f"The student's grade is: {grade}")



#iv)

def grade_students(mark):
    # Check if the mark is a valid number
    if not isinstance(mark, (int, float)):
        return 'invalid Input'
    
    # Check the range of the mark and return the corresponding grade
    if mark >= 90:
        return 'A'
    elif 80 <= mark < 90:
        return 'B'
    elif 70 <= mark < 80:
        return 'C'
    elif 60 <= mark < 70:
        return 'D'
    else:
        return 'F'

# Test with an input that is a number
valid_mark = 85
valid_grade = grade_students(valid_mark)
print(f"Valid Input: {valid_mark} -> Grade: {valid_grade}")

# Test with an input that is not a number
invalid_mark = "eighty-five"
invalid_grade = grade_students(invalid_mark)
print(f"Invalid Input: {invalid_mark} -> Grade: {invalid_grade}")




# #v)

def grade_students(mark):
    # Check if the mark is a valid number
    if not isinstance(mark, (int, float)):
        return 'invalid Input'
    
    # Determine the grade based on the mark
    if mark >= 90:
        grade = 'A'
        message = 'Excellent'
    elif 80 <= mark < 90:
        grade = 'B'
        message = 'Excellent'
    elif 70 <= mark < 80:
        grade = 'C'
        message = 'Good'
    elif 60 <= mark < 70:
        grade = 'D'
        message = 'Satisfactory'
    else:
        grade = 'F'
        message = 'Needs Improvement'
    
    return f"Grade: {grade}, Message: {message}"

# vi) Test with the mark of 78
test_mark = 78
result = grade_students(test_mark)
result
