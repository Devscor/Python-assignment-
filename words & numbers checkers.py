while True:
    print("Menu:")
    print("1. Calculate Sum")
    print("2. Search for a Word")
    print("3. Quit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        numbers = input("Enter numbers separated by spaces: ")
        numbers_list = [float(num) for num in numbers.split()]
        total_sum = sum(numbers_list)
        print(f"The sum of the numbers is: {total_sum}")
    elif choice == '2':
        text = input("Enter a sentence or text: ")
        word_to_search = input("Enter a word to search for: ")
        if word_to_search in text:
            print(f"The word '{word_to_search}' is found in the text.")
        else:
            print(f"The word '{word_to_search}' is not found in the text.")
    elif choice == '3':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
