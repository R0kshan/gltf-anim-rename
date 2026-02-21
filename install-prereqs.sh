#!/bin/bash

if command -v pyenv >/dev/null 2>&1; then
  echo "pyenv is already installed. Version: $(pyenv --version)"
else
  echo "pyenv not found. Installing ..."
  curl -fsSL https://pyenv.run | bash
fi

if command -v python3.8 >/dev/null 2>&1; then
    echo "Python 3.8 is installed at: $(command -v python3.8)"
    echo "Version: $(python3.8 --version)"
else
    echo "Python 3.8 was not found."
    echo "Installing python 3.8 using pyenv ..."
fi
pyenv install 3.8 -s
pyenv local 3.8

echo "Installing venv and the script dependencies." 
python -m venv venv
./venv/bin/pip install -r requirements.txt

echo "All prerequisites installed successfully."

