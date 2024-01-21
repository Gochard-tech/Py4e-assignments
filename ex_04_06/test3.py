largest = None
smallest = None

while True:
    user_input = input("Enter an integer number or 'done' to finish: ")

    if user_input.lower() == 'done':
        break

    try:
        number = int(user_input)
        
        if largest is None or number > largest:
            largest = number
        if smallest is None or number < smallest:
            smallest = number

    except ValueError:
        print("Invalid input. Please enter a valid integer or 'done'.")

if largest is not None and smallest is not None:
    print("Largest:", largest)
    print("Smallest:", smallest)
else:
    print("No valid integers entered.")
