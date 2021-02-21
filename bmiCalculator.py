#!python3
# bmiCalculator.py - calculates Body Mass Index(BMI)

print("**** BMI Calculator ****\n")

weight = float(input("Enter weight(in kg): "))
height_cmeter = float(input("Enter height(in centimeters): "))

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
else:
	print("Enter valid details!")
