signal = input("Enter traffic signal color (red/yellow/green): ").lower()

if signal == "red":
    print("STOP")
elif signal == "yellow":
    print("WAIT")
elif signal == "green":
    print("GO")
else:
    print("Invalid signal color")