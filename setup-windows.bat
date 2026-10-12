@echo off
cd /d %~dp0

where python >nul 2>nul
if errorlevel 1 (
  echo Python is not installed or not in PATH.
  echo Install Python 3.10+ and then run this script again.
  pause
  exit /b 1
)

if not exist ".venv" (
  echo Creating virtual environment...
  python -m venv .venv
)

call .venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install -r backend\requirements.txt
python backend\download_models.py

start "Local AI Backend" cmd /k ".venv\Scripts\activate && python backend\server.py"

echo Setup complete.
echo Open XAMPP Apache and visit: http://localhost:8080/ai-video-studio/
pause
