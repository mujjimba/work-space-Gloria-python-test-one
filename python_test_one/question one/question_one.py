# (a) snake case-student_marks
# (b) camel case- totalAverageMark

#convert the variable
# (ii)
age = 22
age_as_float = float(age)
print(age_as_float)
print(type(age_as_float))


# number 2
def average_of_two_numbers(x, y):
    return (x + y) / 2
#(i)
# Test the function with two different numbers
number1 = 10
number2 = 20

result = average_of_two_numbers(number1, number2)
print("The average of", number1, "and", number2, "is:", result)

# (ii)
# Input from the user
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
number3 = float(input("Enter the third number: "))

# Find the minimum number
minimum = min(number1, number2, number3)

# Display the result
print("The minimum number among", number1, number2, "and", number3, "is:", minimum)


#number 3
# (i)
student_marks = [78, 83, 90, 88, 75]

# Calculate the sum of the items in the list
total_marks = sum(student_marks)

# Print the result with the desired message
print("The sum of the items in the student marks list is:", total_marks)


#(ii)
student_marks = [78, 83, 90, 88, 75]
# Display the first mark
first_mark = student_marks[0]
print("The first mark in the list is:", first_mark)

# Display the last mark
last_mark = student_marks[-1]
print("The last mark in the list is:", last_mark)

#(iii)
student_marks = [78, 83, 90, 88, 75]

# Add 96 to the list
student_marks.append(96)
print("Updated student marks list:", student_marks)


#(iv)
student_marks = [78, 83, 90, 88, 75]

# Update the student mark from 78 to 87
student_marks[0] = 87
print("Updated student marks list:", student_marks)
