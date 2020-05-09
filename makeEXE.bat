d:
cd D:\dev\python3\ak-bb

del *.spec
rd /s /q build 
rd /s /q dist

pyinstaller -F -c -i "ak-bb.ico" "ak-bb.py"

del *.spec
rd /s /q build

pause