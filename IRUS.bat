@echo off
REM IRUS V5.0 - Windows Launcher
REM This batch file launches IRUS with proper error handling

title IRUS V5.0 - Professional Fishing Macro Converter

echo.
echo ========================================
echo    IRUS V5.0 - Windows Launcher
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo.
    echo Please install Python 3.7+ from https://python.org
    echo Make sure to check "Add Python to PATH" during installation
    echo.
    pause
    exit /b 1
)

REM Check if we're in the right directory
if not exist "launch_irus.py" (
    echo ERROR: launch_irus.py not found
    echo.
    echo Please run this batch file from the IRUS directory
    echo.
    pause
    exit /b 1
)

REM Launch IRUS
echo Starting IRUS V5.0...
echo.

python launch_irus.py

REM Check exit code
if errorlevel 1 (
    echo.
    echo ERROR: IRUS failed to start
    echo Check the error messages above for details
    echo.
    pause
    exit /b 1
)

echo.
echo IRUS closed successfully
pause
