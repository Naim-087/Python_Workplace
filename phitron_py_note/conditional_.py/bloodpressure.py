def check_blood_pressure(systolic, diastolic):
    if systolic < 90 or diastolic < 60:
        return "Hypotension (Low)"
    elif systolic < 120 and diastolic < 80:
        return "Normal"
    elif 120 <= systolic <= 129 and diastolic < 80:
        return "Elevated"
    elif (130 <= systolic <= 139) or (80 <= diastolic <= 89):
        return "Stage 1 Hypertension"
    else:
        return "Stage 2 Hypertension"

# Example runs
print(check_blood_pressure(118, 76))  # Normal
print(check_blood_pressure(135, 78))  # Stage 1 Hypertension
print(check_blood_pressure(145, 95))  # Stage 2 Hypertension