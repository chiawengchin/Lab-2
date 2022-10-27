def calculate_bmi(height, weight):
    print ("Height = " + str(height))
    print ("Weight = " + str(weight))

    #Add code here to calculate BMI
    bmi = weight/(height**2)
    print ("BMI = " + str(bmi))

calculate_bmi(weight = 57, height = 1.73)

