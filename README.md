# AI Customer Feedback Analyzer

A Streamlit app that predicts whether a customer review is positive, neutral, or negative.

## Run on Windows

1. Install Python 3.13 or newer.
2. Double-click `run.bat`, or run it from PowerShell:

   ```powershell
   .\run.bat
   ```

The launcher creates a local `.venv` if needed, installs the pinned dependencies, creates the trained model if it is missing, and starts the app. Open the local URL printed in the terminal (usually <http://localhost:8501>).

## Run manually

From the project folder:

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

If `sentiment_model.pkl` is missing, create it before starting the app:

```powershell
python save_model.py
```

## Project contents

- `app.py` — Streamlit user interface.
- `sentiment_model.pkl` — trained sentiment-classification pipeline.
- `data/` — sample customer reviews and prepared datasets.
- `save_model.py` — trains and saves the model from `data/preprocessed_reviews.csv`.
- `text_preprocessing.py` — prepares review text for model training.

The virtual environment and local Python cache files are excluded from Git. Install dependencies from `requirements.txt` after cloning; do not upload the local `.venv` or `venv` folders.

## Publish to GitHub

Create an empty repository on GitHub (without adding a README, `.gitignore`, or license), then run these commands from the project folder. Replace the URL with your repository's URL:

```powershell
git add .
git commit -m "Initial project setup"
git remote add origin https://github.com/<your-username>/<your-repository>.git
git push -u origin main
```
