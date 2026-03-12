import tkinter as tk
from tkinter import messagebox
from utils.inference_engine import diagnose, get_health_tip
from utils.history_logger import save_history

class HealthAssistantApp:
    def __init__(self, root):
        self.root = root
        self.root.title("FOL-Based Health Assistant")
        self.root.geometry("500x400")
        self.root.resizable(False, False)

        tk.Label(root, text="Enter symptoms separated by commas:", font=("Arial", 14)).pack(pady=20)
        self.symptoms_entry = tk.Entry(root, width=60)
        self.symptoms_entry.pack(pady=10)

        tk.Button(root, text="Diagnose", command=self.diagnose, bg="#4CAF50", fg="white", font=("Arial", 12)).pack(pady=10)
        self.result_text = tk.Text(root, height=10, width=60)
        self.result_text.pack(pady=10)

    def diagnose(self):
        symptoms_input = self.symptoms_entry.get()
        conditions = diagnose(symptoms_input)
        self.result_text.delete("1.0", tk.END)

        if conditions:
            output = ""
            for condition in conditions:
                tip = get_health_tip(condition)
                output += f"Condition: {condition.capitalize()}\nTip: {tip}\n\n"
            self.result_text.insert(tk.END, output)
            save_history(symptoms_input, conditions)
        else:
            self.result_text.insert(tk.END, "No matching condition found. Please consult a doctor.")
