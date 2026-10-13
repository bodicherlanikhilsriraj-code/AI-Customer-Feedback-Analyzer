@echo off
setlocal
cd /d "%~dp0"

set "PYTHON=.venv\Scripts\python.exe"
if not exist "%PYTHON%" (
    where py >nul 2>nul
    if not errorlevel 1 (
        py -3.13 -m venv .venv
        if errorlevel 1 py -m venv .venv
    ) else (
        where python >nul 2>nul
        if errorlevel 1 (
            echo Python 3.13 or newer is required. Install it from https://www.python.org/downloads/
            exit /b 1
        )
        python -m venv .venv
    )
    if errorlevel 1 exit /b 1
)

"%PYTHON%" -m pip install -r requirements.txt
if errorlevel 1 exit /b 1

if not exist "sentiment_model.pkl" (
    "%PYTHON%" save_model.py
    if errorlevel 1 exit /b 1
)

"%PYTHON%" -m streamlit run app.py
