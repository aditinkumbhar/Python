print("===== CUSTOMER FEEDBACK FORM ATTER =====")

name = str(input("Enter customer name: "))

feedback = str(input("Enter your feedback: "))

rating = int(input("enter the rating(1 to 5):*"))

name = name.strip()

feedback = feedback.strip()

formatted_name = name.title()

formatted_feedback = feedback.capitalize()

upper_feedback = feedback.upper()

lower_feedback = feedback.lower()

print("\n=====Professional Feedback=====")

print(f"Customer Name : {formatted_name}")

print(f"Feedback       : {formatted_feedback}")

print(f"rating         : {rating}/5")

print(f"\nThank You , {formatted_name},for your valuable feedback.")