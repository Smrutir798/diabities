
def user_enter():
    glucose_range = (80, 180)
    blood_pressure_range = (80, 130)
    skin_thickness_range = (20, 47)
    insulin_range = (90, 168)
    bmi_range = (30, 42)
    age_range = (30, 150)
    glucose = int(input("Enter glucose level (80-180): "))
    blood_pressure = int(input("Enter blood pressure (80-130): "))
    skin_thickness = int(input("Enter skin thickness (20-47): "))
    insulin = int(input("Enter insulin level (90-168): "))
    bmi = int(input("Enter BMI (30-42): "))
    age = int(input("Enter age (30 to 150): "))

    if not (glucose_range[0] <= glucose <= glucose_range[1]):
        print("Glucose level out of range")
    elif not (blood_pressure_range[0] <= blood_pressure <= blood_pressure_range[1]):
        print("Blood pressure out of range")
    elif not (skin_thickness_range[0] <= skin_thickness <= skin_thickness_range[1]):
        print("Skin thickness out of range")
    elif not (insulin_range[0] <= insulin <= insulin_range[1]):
        print("Insulin level out of range")
    elif not (bmi_range[0] <= bmi <= bmi_range[1]):
        print("BMI out of range")
    elif not (age_range[0] <= age <= age_range[1]):
        print("Age out of range")
    else:

        if glucose > 150 and blood_pressure < 110 and skin_thickness > 40 and insulin < 120 and bmi < 35 and age > 35:
            print("The person is diabetic")
        elif glucose > 150 and blood_pressure > 120 and skin_thickness < 30 and insulin > 120 and bmi > 40 and age < 35:
            print("The person is not diabetic")
        elif glucose < 140 and blood_pressure > 120 and skin_thickness > 43 and insulin < 100 and bmi < 40 and age < 50:
            print("The person is diabetic")
        elif glucose < 130 and blood_pressure < 95 and skin_thickness < 32 and insulin > 135 and bmi < 38 and age < 70:
            print("The person is diabetic")
        elif glucose < 128 and blood_pressure > 125 and skin_thickness > 45 and insulin > 148 and bmi < 31 and age < 40:
            print("The person is not diabetic")
        elif glucose > 165 and blood_pressure > 125 and skin_thickness < 28 and insulin > 155 and bmi > 41 and age > 75:
            print("The person is diabetic")
        elif glucose > 178 and blood_pressure < 115 and skin_thickness > 38 and insulin < 95 and bmi == 42 and age < 78:
            print("The person is diabetic")
        else:
            print("The person is not diabetic")
            
user_enter()