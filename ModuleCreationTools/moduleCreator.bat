@echo off
setlocal

set "name=%~1"

mkdir "..\KrakenModules\%name%"
copy ".\templateFiles\main.py" "..\KrakenModules\%name%\main.py"
copy ".\templateFiles\module.ini" "..\KrakenModules\%name%\module.ini"

endlocal
