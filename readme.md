# FOL-Based Health Assistant GUI

A lightweight Tkinter desktop app that uses simple rule-based inference (FOL-style symptom matching) to suggest health conditions and tips, plus logs diagnosis history.

## 🚀 Project structure

- `main.py` – app entry point
- `modules/health_gui.py` – Tkinter UI and control logic
- `utils/inference_engine.py` – symptom→condition inference + health tips
- `utils/history_logger.py` – save diagnosis history (`diagnosis_history.txt`)
- `diagnosis_history.txt` – persisted history output

## 🛠️ Setup

1. Use Python 3.8+ (recommended 3.10+)
2. Clone repo:
   ```bash
   git clone <repo-url>
   cd fol_health_assistant_gui
   ```
3. Run the project  
     python main.py 
  
## 💡 Usage

Enter symptoms separated by commas, e.g.:
fever, cough, sore throat
Click Diagnose
View conditions and tips
History is recorded to diagnosis_history.txt

## 🧩 Notes

utils and modules are packages (__init__.py added).
If Import "utils..." issues appear, run from project root.
For debugging:
python -c "import utils.inference_engine as ie; print(ie.__file__)"
