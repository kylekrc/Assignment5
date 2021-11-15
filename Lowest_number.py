# Program 2: Find the lowest number
# Create a program that ask 3 numbers. 
# Find the lowest number using only if-else statement.
# Display the lowest number


print("Welcome!")
print("Input three (3) numbers of your choice and the program will display the lowest.")


numb_1 = float(input("Enter 1st number: "))
numb_2 = float(input("Enter 2nd number: "))
numb_3 = float(input("Enter 3rd number: "))


if numb_1 < numb_2 < numb_3:
    print(f"The lowest number is {numb_1}.")
elif numb_1 > numb_2 < numb_3:
    print(f"The lowest number is {numb_2}.")
elif numb_1 > numb_2 > numb_3:
    print(f"The lowest number is {numb_3}.")
    
