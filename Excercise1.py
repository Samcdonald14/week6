def sum_of_even_numbers():
    # Get the user input for the number n
    n = int(input("Enter a number: "))

    # Initialize the sum to 0
    even_sum = 0

    # Loop through numbers from 1 to n
    for num in range(1, n + 1):
        # Check if the number is even
        if num % 2 == 0:
            even_sum += num  # Add the even number to the sum

    # Output the result
    print(f"The sum of all even numbers from 1 to {n} is: {even_sum}")


# Call the function to run the program
sum_of_even_numbers()



