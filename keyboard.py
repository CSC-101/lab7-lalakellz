from convert import str_to_float

# Function: Gathers numbers from the user until 'done' is entered
# Input: No input
# Output: List of floats that the user has entered
def gather_numbers() -> list[float]:
    numbers = []
    while True:
        user_input = input("Enter a number, type 'done' when finished: ")
        # check for exit condition
        if user_input.lower() == "done":
            break
        # try to convert to float and add to list if valid
        number = str_to_float((user_input))
        if number is not None:
            numbers.append(number)
        else:
            print("Invalid input.")
    return numbers

if __name__ == '__main__':
    numbers = gather_numbers()
    print("Sum of numbers:", sum(numbers))