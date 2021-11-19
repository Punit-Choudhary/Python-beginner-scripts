#!python3
# bmiCalculator.py - calculates Body Mass Index(BMI)

while(True):
    print("**** BMI Calculator ****\n")

    weight = input("Enter weight(in kg): ")
    height_cmeter = input("Enter height(in centimeters): ")

    try:
        weight = float(weight)
        height_cmeter = float(height_cmeter)

        height = height_cmeter/100  # converting height into meter

        bmi = weight/(height ** 2)

        if bmi > 0:
            print(f"Your current BMI is {bmi}\n")

            if bmi <= 16:
                print("You are severly underweight!")
            elif bmi <= 18.5:
                print("You are underweight!")
            elif bmi <= 25:
                print("You are healthy!")
            elif bmi <= 30:
                print("You are overweight!")
            else:
                print("You are severly overweight!")
    except Exception as e:
        print(f"Enter a valid datails! {e}")
    else:
        print("\n")