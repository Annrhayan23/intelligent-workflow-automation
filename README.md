

# Intelligent Workflow

A **Streamlit-based application** for intelligent workflow management. This project provides a user-friendly interface to interact with backend processes, manage data, and visualize insights.

---

## Features

* Interactive Streamlit app for workflow management
* Integration with backend and utility modules
* Data handling and processing from `data/` folder
* Modular project structure for easy maintenance

---

## Project Structure

```
intelligent_workflow_corrected/
│
├─ intelligent_workflow/
│  ├─ app.py               # Main Streamlit app
│  ├─ backend/             # Backend logic and services
│  ├─ data/                # Data files
│  ├─ utils/               # Utility functions
│  ├─ __init__.py
│  └─ requirements.txt     # Python dependencies
│
├─ venv/                   # Virtual environment
```

---

## Installation

1. **Clone the repository** or download the folder:

```powershell
git clone intelligent-workflow-automation

cd intelligent_workflow_corrected
```

2. **Create and activate a virtual environment** (if not already):

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1  # Windows PowerShell
```

3. **Install dependencies**:

```powershell
pip install --upgrade pip
pip install -r .\intelligent_workflow\requirements.txt
```

---

## Running the App

From the project root directory:

```powershell
streamlit run .\intelligent_workflow\app.py
```

Or navigate into the `intelligent_workflow` folder first:

```powershell
cd .\intelligent_workflow
streamlit run app.py
```

Then open the browser link provided by Streamlit (usually `http://localhost:8501`).

---

## Dependencies

* Python 3.10+
* Streamlit
* Other dependencies listed in `requirements.txt`

---

## Notes

* Make sure your virtual environment is activated before running the app.
* Place any required data files inside the `data/` folder.
* Modify `backend/` and `utils/` modules to customize app logic.

* PICTURES:

<img width="1910" height="900" alt="image" src="https://github.com/user-attachments/assets/7e1213fa-c781-49fc-9a0e-beab47248aa5" />
<img width="1181" height="848" alt="image" src="https://github.com/user-attachments/assets/a4f7f84c-0e48-4fc7-8b26-8747644dd654" />
<img width="1368" height="796" alt="image" src="https://github.com/user-attachments/assets/ba490e42-e1c6-43f4-8c43-9ff3df9c9c40" />
<img width="1120" height="861" alt="image" src="https://github.com/user-attachments/assets/f74e6af2-d337-4b81-96c2-dd8cb8ab71c0" />
<img width="965" height="536" alt="image" src="https://github.com/user-attachments/assets/5bb597e2-6466-4a6e-84ac-2215ac0eec0f" />





