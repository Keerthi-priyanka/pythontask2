print("BIM CALCULATOR")
print("--------------")
weight =float(input("Enter your weight in Kilograms"))
height = float(input("Enter your heigh in cm"))
height_in_meters = float(height/100)
BMI =weight/(height_in_meters**2)
if BMI<18.5:
    category = "Underweight"
elif 18.5 <= BMI < 24.9:
    category = "Normal weight"
elif 25 <= BMI < 29.9:
    category = "Overweight"
else:
    category = "Obese"
    print("\nYour BMI is: {:.2f}".format(BMI))
print("BMI Category: ", category)