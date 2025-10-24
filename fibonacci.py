#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)
def get_positive_integer():
    "Prompt the user until a valid positive integer is entered."
    while True:
        try:
            num = int(input("Enter the number of Fibonacci terms you want: "))
            if num > 0:
                return num
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

def generate_fibonacci(n):
    "Generate the Fibonacci sequence up to n terms."
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def print_sequence(sequence):
    "Print the Fibonacci sequence in a readable format."
    print("Fibonacci sequence:")
    print(", ".join(str(num) for num in sequence))

# Main program flow
terms = get_positive_integer()
fib_sequence = generate_fibonacci(terms)
print_sequence(fib_sequence)
