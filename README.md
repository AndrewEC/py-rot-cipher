# rot-cipher
A POC Python implementation of a rotational cipher that tries to overcome the most common pitfalls of using a
simple rotational cipher without making the implementation overly complicated.

## Usage
Run the powershell script `CreateVenv.ps1` to create a virtual environment which will install the required Click
dependency as well as the rotcipher package.

After installation, you can apply and reverse the rotational cipher on a string using
`python run.py apply string_to_encode` and `python run.py reverse string_to_decode` respectively.

Additionally, you can apply and reverse a versioned rotational cipher on a string using
`python run.py apply-versioned A string_to_encode` and `python run.py reverse-versioned string_to_decode`
respectively.

## Unit Tests
First, you should run the `CreateVenv.ps1` script to activate or create the virtual environment then run the command
`python -m unittest rotcipher.tests.__run_all` to execute all unit tests.
