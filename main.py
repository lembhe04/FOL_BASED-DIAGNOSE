import tkinter as tk
from tkinter import messagebox
from modules.health_gui import HealthAssistantApp

def main():
    root = tk.Tk()
    app = HealthAssistantApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
