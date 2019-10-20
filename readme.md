
## Upgrade pip
python3 -m pip install --upgrade pip

## Create Virtual Env named env
python3 -m venv env

## Activate virtual env
source env/bin/activate

## Update pip of virtual env
python3 -m pip install --upgrade pip

## Install dependencies
pip install -r requirements.txt

# How to Run
## Mode: file_input.txt

python parking_lot.py file_inputs.txt

## Mode: Interactive

python parking_lot.py 

### To return out of interactive mode type 'exit'

exit

## Command to Run Tests
python3 -m unittest

## build library

pyinstaller parking_lot.py