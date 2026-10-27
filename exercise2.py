# Question 1: Arithmetic and Assignment Operators
x = 8
y = 10
x += 4
y *= 2
result = x / y
print(result)
# Question 2: Comparison and Logical Operators
a = 15 
b = 8 
c = 10
condition1 = a > b 
condition2 = b % 2 == 0
condition3 = c <= a 
final_condition = condition1 or (condition2 and condition3)
print(f"Q2 Final Condition: {final_condition}")
# Question 3: Conditional Statements
score = 80 
if 90 <= score <= 100:
    grade = "A"
elif 80 <= score <= 89:
    grade = "B"    
elif 70 <= score <= 79:
    grade = "C"
elif 60 <= score <= 69:
    grade = "D"
else: 
    grade = "F"
print(f"Q3 Grade: {grade}")    
# Question 4: Combining Operators and Conditionals
num1 = 4
num2 = 2
operation = input("operation (+, -, *, /): ")
if operation == "+":
    result = num1 + num2 
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0: 
        result = num1 / num2
    else:
        result = "Error: Cannot divide by zero"
else:
    result = "Invalid operation"
print("Q4 Result", result)