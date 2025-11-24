import csv
import os

def heart_attack_check():
    print("Welcome to the Heart Attack Risk Checkup!")
    print("Please answer the following questions honestly to assess your medical condition .")


    try:
        age = int(input("Enter your age: "))
        chest_pain = input("Do you experience chest pain? (yes/no): ").strip().lower()
        blood_pressure_systolic = int(input("Enter your systolic blood pressure (top number): "))  
        blood_pressure_diastolic = int(input("Enter your diastolic blood pressure (bottom number): ")) 
        cholesterol = int(input("Enter your cholesterol level (in mg/dL): "))
        diabetes = input("Do you have diabetes? (yes/no): ").strip().lower()
        family_history = input("Is there a family history of heart disease? (yes/no): ").strip().lower()
        physical_activity = input("Do you engage in regular physical activity? (yes/no): ").strip().lower()
        obesity = input("Are you obese? (yes/no): ").strip().lower()
        smoking = input("Do you smoke? (yes/no): ").strip().lower()
    except ValueError:
        print("Invalid input. Please enter the correct data types.")
        return


    risk_score = 0
    if age > 45:
        risk_score += 2
    if chest_pain == 'yes':
        risk_score += 3
    if blood_pressure_systolic > 130 or blood_pressure_diastolic > 80:
        risk_score += 2 
    if cholesterol > 200:
        risk_score += 2
    if diabetes == 'yes':
        risk_score += 2
    if smoking == 'yes':
        risk_score += 2
    if family_history == 'yes':
        risk_score += 1
    if physical_activity == 'no':
        risk_score += 1 
    if obesity == 'yes':
        risk_score += 2 

    print("Calculating your heart attack risk...")    
    if risk_score >= 10:
        risk_level = "High Risk"
    elif risk_score >= 5:
        risk_level = "Moderate Risk"
    else:
        risk_level = "Low Risk" 
    print("Your Heart Attack Risk Level: ",risk_level)
    if risk_level == "High Risk":
        print("  Warning: You are at High Risk for a heart attack. Please seek immediate medical attention.")
    elif risk_level == "Moderate Risk":
        print("  Caution: You are at Moderate Risk for a heart attack. Consider lifestyle changes and consult a healthcare professional.")
    elif risk_level == "Low Risk":
        print(" Good News: You are at Low Risk for a heart attack. Maintain a healthy lifestyle to keep your risk low.")

    filename = 'heart_risk_data.csv'

    fieldnames = [
        'Age',
        'Chest Pain',
        'Systolic BP',
        'Diastolic BP', 
        'Cholesterol',
        'Diabetes',
        'Family History',
        'Physical Activity',
        'Obesity',
        'Smoking',
        'Risk Level',
    ]

    row = {
        'Age': age ,
        'Chest Pain': chest_pain,
        'Diastolic BP' : blood_pressure_diastolic,
        'Systolic BP': blood_pressure_systolic,
        'Cholestrol': cholesterol,
        'Diabetes': diabetes,
        'Family Activity': family_history,
        'Physical Activity': physical_activity,
        'Obesity':obesity,
        'Smoking': smoking,
        'Risk Level': risk_level
    }

    file_exists = os.path.exists(filename)


    with open(filename , mode='a',newline=' ') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)


        if not file_exists:
            writer.writeheader()


        writer.writerow(row)

    print("your data has been saved to", filename)


if __name__ == "__main__":
    heart_attack_check()