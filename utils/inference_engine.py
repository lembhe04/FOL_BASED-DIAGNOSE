rules = [
    { "if": ["fever", "cough"], "then": "flu" },
    { "if": ["fever", "cough", "loss_of_taste"], "then": "covid-19" },
    { "if": ["chest_pain", "short_breath"], "then": "pneumonia" },
    { "if": ["headache", "nausea"], "then": "migraine" },
    { "if": ["sore_throat", "fever"], "then": "throat_infection" },
]

health_tips = {
    "flu": "Drink plenty of fluids and get rest.",
    "covid-19": "Isolate and consult a doctor immediately.",
    "pneumonia": "Seek medical attention and avoid cold environments.",
    "migraine": "Rest in a dark room and avoid loud noises.",
    "throat_infection": "Gargle with warm salt water and stay hydrated.",
}

def diagnose(symptoms_input):
    symptoms = [s.strip().lower().replace(" ", "_") for s in symptoms_input.split(",")]
    possible_conditions = []

    for rule in rules:
        if all(symptom in symptoms for symptom in rule["if"]):
            possible_conditions.append(rule["then"])

    return possible_conditions

def get_health_tip(condition):
    return health_tips.get(condition.lower(), "")
