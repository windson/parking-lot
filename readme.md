# Parking Lot Problem Solution
Author: Navule Pavan Kumar Rao

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

## Generate executable

pyinstaller parking_lot.py

### copy the contents of the generate dist/parking_lot directory to the gojek provided bin directory and read the instructions mentioned in How to run.md

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


## Code Coverage report
### Step 1:
Run `coverage run parking_lot.py file_inputs.txt`
### Step 2:
Run `coverage run parking_lot.py` and play with edge cases

### Finally generate report command

`coverage report -m`

```
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
input_processor.py           90     19    79%   29-32, 35-43, 53, 62, 92, 98, 123, 127-128
models/__init__.py            0      0   100%
models/car.py                 8      0   100%
models/slot.py               16      0   100%
parking_lot.py               14      2    86%   15-17
service/__init__.py           0      0   100%
service/lot_handler.py       64      4    94%   25, 47-49
service/park_service.py      60     17    72%   16, 23, 26, 51, 59, 66, 71-75, 83, 91, 95, 100-103
util/__init__.py              0      0   100%
util/constants.py            14      0   100%
-------------------------------------------------------
TOTAL                       266     42    84%
```

## Generate HTML Code coverage Report
`coverage html -d coverage_html`

Html report located in `coverage_html\index.html` directory
