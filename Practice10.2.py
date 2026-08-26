product = ["Laptop","Mouse","Keyboard","CPU","Mobile"]
item = input("Enter the product name to search: ")
if item in product:
    index=product.index(item)
    print(f"{item} is available in inventory")
    print(f"index location: {index}")
else:
    print(f"{item} is not available in inventory")