@echo off
pip install pyinstaller
pyinstaller --onefile --noconsole inventory_finance_plus_app.py
pause
