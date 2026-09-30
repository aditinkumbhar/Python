print("PHONEBOOK / WORD FREQUENCY APP")

phonebook = {}
word_freq = {}

while True:
    print("\n1. Add Contact")
    print("2. Search Contact")
    print("3. Display Contacts")
    print("4. Delete Contact")
    print("5. Word Frequency")
    print("6. Display Word Frequency")
    print("7. Exit")

    choice = input("Enter choice: ")

    # Add Contact
    if choice == "1":
        name = input("Enter name: ")
        number = input("Enter number: ")

        phonebook[name] = number
        print("Contact added.")

    # Search Contact
    elif choice == "2":
        name = input("Enter name: ")

        if name in phonebook:
            print("Number:", phonebook[name])
        else:
            print("Contact not found.")

    # Display Contacts
    elif choice == "3":
        if len(phonebook) == 0:
            print("Phonebook is empty.")
        else:
            for name in phonebook:
                print(name, ":", phonebook[name])

    # Delete Contact
    elif choice == "4":
        name = input("Enter name: ")

        if name in phonebook:
            del phonebook[name]
            print("Contact deleted.")
        else:
            print("Contact not found.")

    # Word Frequency
    elif choice == "5":
        paragraph = input("Enter paragraph: ").lower()

        for symbol in ".,!?;:'\"()":
            paragraph = paragraph.replace(symbol, "")

        words = paragraph.split()

        word_freq = {}

        for word in words:
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1

        print("Word frequency calculated.")

    # Display Word Frequency
    elif choice == "6":
        if len(word_freq) == 0:
            print("No data available.")
        else:
            for word in word_freq:
                print(word, ":", word_freq[word])

            most_common = max(word_freq, key=word_freq.get)
            print("Most frequent word:", most_common)

    # Exit
    elif choice == "7":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")