@echo off
python business_logic/if_first_start.py
python tests/test.py -v
pause
python view/table.pyw
