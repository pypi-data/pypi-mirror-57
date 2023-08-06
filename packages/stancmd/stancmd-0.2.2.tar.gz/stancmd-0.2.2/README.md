# Stan

## Requirements
* Python 3

## What is Stan ?
Stan is a simple python package / script that launches the command you pass it
after waiting four hours. However, as it calls `subprocess` it does **not**
handle aliases or shell builtins. It also catches some signals in order to keep
waiting.

## Usage
### As a script
`./stan.py cmd`