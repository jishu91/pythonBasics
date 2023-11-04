def sum_of_digits(number):
    # Convert the number to a string to iterate through its digits
    num_str = str(number)
    
    # Initialize a variable to store the sum
    digit_sum = 0
    
    # Iterate through each digit and add it to the sum
    for digit in num_str:
        if digit.isdigit():  # Check if the character is a digit
            digit_sum += int(digit)
    
    return digit_sum

# Test cases
number1 = 12345
number2 = 9876

print("Sum of digits for", number1, "is", sum_of_digits(number1))
print("Sum of digits for", number2, "is", sum_of_digits(number2))
