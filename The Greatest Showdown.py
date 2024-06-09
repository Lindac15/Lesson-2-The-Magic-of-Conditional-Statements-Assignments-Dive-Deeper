# Task 1: Identify the Greatest

number_1 = input("Enter the first number:")
number_2 = input("Enter the second number:")
number_3 = input("Enter the third number:")
print("The numbers are:",number_1,number_2,number_3)

if number_1 > number_2 and number_1 > number_3:
    print("The greatest number is:", number_1)
elif number_2 > number_1 and number_2 > number_3:
    print("The greatest number is:", number_2)
else:
    print("The greatest number is:",number_3)

# Task 2: Identify the Smallest

number_1 = input("Enter the first number:")
number_2 = input("Enter the second number:")
number_3 = input("Enter the third number:")
print("The numbers are:",number_1,number_2,number_3)

if number_1 < number_2 and number_1 < number_3:
    print("The smallest number is:", number_1)
elif number_2 < number_1 and number_2 < number_3:
    print("The smallest number is:", number_2)
else:
    print("The smallest number is:",number_3)

# Task 3: Equality Check

number_1 = input("Enter the first number:")
number_2 = input("Enter the second number:")
number_3 = input("Enter the third number:")
print("The numbers are:",number_1,number_2,number_3)

if number_1 == number_2 == number_3:
    print("All numbers are equal.") 
elif number_1 == number_3 and number_1 > number_2:
    print(number_1, "and", number_3, "are equal and the greatest numbers. The smallest number is:", number_1)
elif number_1 == number_3 and number_1 < number_2:
    print(number_1, "and", number_3, "are equal and the smallest numbers. The greatest number is:", number_2)   
elif number_1 == number_2 and number_2 > number_3:
    print(number_1, "and", number_2, "are equal and the greatest values. The smallest number is:", number_3)
elif number_1 == number_2 and number_2 < number_3:
    print(number_1, "and", number_2, "are equal and the smallest values. The greatest number is:", number_3)
elif number_2 == number_3 and number_2 > number_1:
    print(number_2, "and", number_3, "are equal and the greatest numbers. The smallest number is:", number_1)
elif number_2 == number_3 and number_2 < number_1:
    print(number_2, "and", number_3, "are equal and the smallest numbers. The greatest number is:", number_1)   
else:
    print("No numbers are equal.")
    
