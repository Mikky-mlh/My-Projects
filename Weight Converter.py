while True:
    try:
        weight = float(input("Enter weight:"))
        if weight < 0:
            print("Weight cannot be negative.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

while True:
    try:
        unit = input("Enter unit (Lbs or Kgs): ").strip().lower()
        if unit not in ["Lbs", "lbs", "pounds", "kilograms", "kgs", "kg", "pound", "kilogram", "lb",]:
            print("Invalid unit. Please enter 'pounds' or 'kilograms'.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid unit.")

# Convert weight to kilograms
if unit in ["Lbs", "lbs", "pounds", "lb"]:
    weight_kg = weight * 0.45359237
    print(f"Your weight of {weight} pounds is equal to {weight_kg:.2f} kilograms.")
else:
    print(f"Your wight is {weight} kilograms.")  # No conversion needed for kg