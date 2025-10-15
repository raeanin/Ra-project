
N = int(input("Enter a three-digit number: "))


if 100 <= N <= 999:
    
    hundreds = N // 100
    tens = (N // 10) % 10
    units = N % 10

    
    digit_sum = hundreds + tens + units

    
    if digit_sum % 2 == 0:
        print("The sum of digits is even.")
    else:
        print("The sum of digits is odd.")
else:
    print("Error: Please enter a valid three-digit number.")
