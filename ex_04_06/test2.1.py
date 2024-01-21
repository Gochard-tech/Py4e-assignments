total = 0
count = 0

while True:
    user_input = input("Enter a number or 'done' to finish: ")

    if user_input.lower() == 'done':
        if count == 0:
            print("You haven't entered any numbers. Please enter at least one number.")
            continue
        else:
            break

    try:
        number = float(user_input)
        total += number
        count += 1
    except ValueError:
        print("Invalid input. Please enter a number or 'done'.")

if count > 0:
    average = total / count
    print("Total:", total)
    print("Count:", count)
    print("Average:", average)
else:
    print("No valid numbers entered.")
