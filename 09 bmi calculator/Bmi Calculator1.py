height_cm = float(input("Enter your height in cm: "))
weight_kg = float(input("Enter your weight in kg: "))

height_m = height_cm / 100


bmi = weight_kg / (height_m ** 2)


print(f"Your BMI is: {bmi:.2f}")


if bmi > 0:
    if bmi <= 16:
        print("Severely underweight")
    elif bmi <= 18.5:
        print("Underweight")
    elif bmi <= 25:
        print("Healthy")
    elif bmi <= 30:
        print("Overweight")
    else:
        print("Severely overweight")
else:
    print("Please enter valid information")
