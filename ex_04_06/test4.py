largest = None
smallest = None
my_list = []

try:
    num_entries = int(input("Enter the number of integer values you want to input: "))
except ValueError:
    print("Invalid input. Please enter a valid integer for the number of entries.")
    exit()

for _ in range(num_entries):
    user_input = input("Enter an integer number or 'done' to finish: ")
    

    if user_input.lower() == 'done':
        break

    try:
        number = int(user_input)

        

        if largest is None or number > largest:
            largest = number
        if smallest is None or number < smallest:
            smallest = number

        my_list.append(_)

    except ValueError:
        print("Invalid input. Please enter a valid integer or 'done'.")
print(my_list)

if largest is not None and smallest is not None:
    print("Largest:", largest)
    print("Smallest:", smallest)
else:
    print("No valid integers entered.")
