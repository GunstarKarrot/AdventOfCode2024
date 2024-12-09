@echo off

:: Check if a directory parameter is provided
if "%~1"=="" (
    echo Usage: %~nx0 ^<directory^>
    exit /b 1
)
set CWD=%CD%
:: Change to the specified directory
cd /d "%~1" || exit /b 1

:: Extract the TargetFramework from the .csproj file
for /f "tokens=2 delims=<>" %%i in ('findstr /i /c:"<TargetFramework>" *.csproj') do set "DOTNET_VERSION=%%i"

:: Set the environment variable
set DOTNET_VERSION=%DOTNET_VERSION%

:: Print the environment variable to verify
echo -n %DOTNET_VERSION% > %CWD%\\.vscode\\dotnet-version.txt