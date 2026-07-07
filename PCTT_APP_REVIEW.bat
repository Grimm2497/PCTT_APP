@echo off
setlocal EnableExtensions
cd /d "%~dp0"

REM ==========================================================
REM BTS PCTT - WEB ONE CLICK RUNNER
REM - Tu tao .venv neu chua co
REM - Tu cai/cap nhat thu vien neu thieu
REM - Mo giao dien web Streamlit tren trinh duyet
REM ==========================================================

set "APP_FILE=%~dp0app.py"
set "VENV_PY=%~dp0.venv\Scripts\python.exe"
set "REQ_FILE=%~dp0requirements.txt"
set "FAST_MODE=1"

if not exist "%APP_FILE%" (
    echo Khong tim thay app.py trong thu muc hien tai.
    echo Hay giai nen day du bo tool roi chay lai.
    pause
    exit /b 1
)

set "VENV_READY=0"
if exist "%VENV_PY%" (
    "%VENV_PY%" -c "import sys" >nul 2>nul
    if errorlevel 1 (
        echo Moi truong .venv cu bi loi. Dang doi ten va tao lai...
        ren ".venv" ".venv_broken_%RANDOM%"
        if errorlevel 1 (
            echo Khong doi ten duoc .venv cu. Hay dong cac cua so Python/Streamlit roi chay lai.
            pause
            exit /b 1
        )
    ) else (
        set "VENV_READY=1"
    )
)

if "%VENV_READY%"=="0" (
    python --version >nul 2>nul
    if errorlevel 1 (
        echo Khong chay duoc Python tren may.
        echo Vui long cai Python 3.10+ va tick Add Python to PATH, sau do chay lai file nay.
        pause
        exit /b 1
    )
)

if not exist "%VENV_PY%" (
    echo Lan dau chay tool - dang tao moi truong ao .venv...
    python -m venv .venv
    if errorlevel 1 (
        echo Tao .venv that bai. Hay chay bang quyen Administrator hoac kiem tra Python.
        pause
        exit /b 1
    )
)

call "%~dp0.venv\Scripts\activate.bat"

REM Kiem tra nhanh cac goi bat buoc. Neu thieu thi tu cai requirements.
python -c "import streamlit, pandas, openpyxl, docx, pypdf, xlsxwriter, dotenv, tabulate, rapidfuzz, openai" >nul 2>nul
if errorlevel 1 (
    echo Dang cai/cap nhat thu vien can thiet, vui long doi...
    python -m pip install --upgrade pip
    pip install -r "%REQ_FILE%"
    if errorlevel 1 (
        echo Cai thu vien that bai. Hay kiem tra mang hoac chay run_desktop_debug.bat de xem loi chi tiet.
        pause
        exit /b 1
    )
)

echo Dang mo giao dien web PCTT_APP_REVIEW...
echo Neu trinh duyet khong tu mo, truy cap: http://localhost:8501
python -m streamlit run "%APP_FILE%" --server.address localhost --server.port 8501

pause
