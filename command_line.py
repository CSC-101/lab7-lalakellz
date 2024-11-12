import sys
from convert import str_to_float

# Function: converts a list of command-line arguments to floats
# Input: list of str
# Output: sum of valid floats in the input list
def sum_command_line_numbers(args: list[str]) -> float:
    numbers = []
    for arg in args:
        number = str_to_float(arg)
        if number is not None:
            numbers.append(number)
    return sum(numbers)

if __name__ == '__main__':
    total = sum_command_line_numbers(sys.argv[1:])
    print("Sum of numbers:", total)