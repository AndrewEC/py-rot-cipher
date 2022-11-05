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

## Quality Metrics
Before running any of the scripts or commands listed below you should create or activate the appropriate virtual
environment using the script `CreateVenv.ps1`.

## Unit Tests
Execute the unit tests and generate a code coverage report:
> Coverage.ps1

Alternatively you can execute unit tests without any code coverage:
> python -m unittest rotcipher.tests.__run_all

## Mutation Test
Execute the mutation tests and view the kill count report:
> Mutations.ps1

## Linting
To run flake8 and view the results:
> flake8