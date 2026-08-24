# Invoice Pattern

n = int(input("Enter number of rows: "))

print("\nINVOICE")

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

# Receipt Number Pattern

n = int(input("Enter number of rows: "))

print("\nRECEIPT")

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()