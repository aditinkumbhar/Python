print("******MONTHLY EXPENSE TRACKER*****")

n=int(input("Enter the number of expenses: "))

expenses = []
total = 0

for i in range(n):
    amount = float(input(f"Enter expense {i + 1}: "))
    expenses.append(amount)
    total += amount

while True:
    print("\n-----Expense Tracker Menu-----")
    print("1. Show all expenses")
    print("2. Show Total expenses")
    print("3. Add new expenses")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("\nExpense List: ")
        for i in range(len(expenses)):
            print(f"Expense {1 + i}: {expenses[i]}")

    elif choice == 2:
        print("Total Monthly Expense =", total)

    elif choice == 3:
        new_expense = float(input("Enter new expense: "))
        expenses.append(new_expense)
        total += new_expense
        print("Expense added successfully.")

    elif choice == 4:
        print("thank you for using the Monthly Expense Tracker!")
        break

    else:
        print("Invalid choice! Please try again.")