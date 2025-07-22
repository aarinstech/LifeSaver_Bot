@echo off
curl -o python-installer.exe https://www.python.org/ftp/python/3.12.1/python-3.12.1-amd64.exe
python-installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_pip=1
pause