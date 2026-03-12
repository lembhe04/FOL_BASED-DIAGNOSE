import datetime

def save_history(symptoms, conditions):
    with open("diagnosis_history.txt", "a") as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{timestamp}] Symptoms: {symptoms} -> Conditions: {', '.join(conditions)}\n")
