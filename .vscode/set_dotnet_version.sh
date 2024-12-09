#!/bin/bash

# Check if a directory parameter is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <directory>"
  exit 1
fi
cwd=$(pwd)
# Change to the specified directory
cd "$1" || exit

# Extract the TargetFramework from the .csproj file
TARGET_FRAMEWORK=$(grep -oPm1 "(?<=<TargetFramework>)[^<]+" *.csproj)

# Print the environment variable to verify
echo -n "$TARGET_FRAMEWORK" > $cwd/.vscode/dotnet-version.txt