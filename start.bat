@echo off
title Finairis Dev Launcher

echo ==================================
echo  Finairis Auto Launcher
echo ==================================

echo.
echo [1/2] Starting backend (FastAPI)...
start "Backend" cmd /k "cd backend && uvicorn main:app --reload --host 127.0.0.1 --port 8000"

timeout /t 3 >nul

echo [2/2] Starting Electron frontend...
start "Electron" cmd /k "cd frontend && npx electron ."

echo.
echo DONE - all services started 🚀