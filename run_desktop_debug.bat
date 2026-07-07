@echo off
setlocal EnableExtensions
cd /d "%~dp0"
set "FAST_MODE=1"

if not exist ".venv\Scripts\python.exe" (
    echo Chua co .venv. Dang tao va cai thu vien...
    python -m venv .venv
)
call ".venv\Scripts\activate.bat"
python -m pip install --upgrade pip
pip install -r requirements.txt
python desktop_app.py
pause
