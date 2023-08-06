# Stan

## Requirements
* Python 3

## What is Stan ?
Stan is a simple python package / script that launches the command you pass it
after waiting four hours. However, as it calls `subprocess` it does **not**
handle aliases or shell builtins. It also catches some signals in order to keep
waiting.

## Installation
`pip install --user stancmd`

## Usage

### As a script (after cloning the repo)
`./stancmd/stan.py cmd`

### As a package (after installing via pip)
`stancmd cmd`
