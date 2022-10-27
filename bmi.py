def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    # Add code here to calculate BMI
    bmi = weight / (height ** 2)
    print("BMI = " + str(bmi))

    # Categorize the BMI
    if bmi < 18.5:
        print("Underweight!")
    elif bmi >= 18.5 or bmi <= 25.0:
        print("Normal Weight!")
    else:
        print("Overweight!")


calculate_bmi(weight=57, height=1.73)
