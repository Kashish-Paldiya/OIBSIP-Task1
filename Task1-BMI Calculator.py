def bmi_calculation(weight, height):
    try:
        weight = float(weight)
        height = float(height)
    except ValueError:
        print("Invalid input. Please enter numeric values for weight and height.")
        return None

    if height <= 0 or weight <= 0:
        print("Height and Weight cannot be negative. Please enter positive values.")
        return None

    bmi = weight / (height ** 2)

    return bmi


def bmi_categories(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"


def main():
    print("BMI Calculator")
    print("---------------")

    weight = input("Enter your weight in kilograms: ")
    height = input("Enter your height in meters: ")

    bmi = bmi_calculation(weight, height)

    if bmi is not None:
        print("\nYour BMI is: ",bmi)
        category = bmi_categories(bmi)
        print("You are classified as: ",category)


if __name__ == "__main__":
    main()
