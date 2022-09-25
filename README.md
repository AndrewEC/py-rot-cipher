# rot-cipher
A POC Python implementation of a rot cipher that tries to overcome the most common pitfalls of using a
simple rotational cipher without making the implementation overly complicated.

## Usage
Run the powershell script `CreateVenv.ps1` to create a virtual environment which will install the required Click
dependency as well as the rocipher package.

After installation you can apply and reverse the ciphered string using `python run.py apply &lt;value&gt;` and
`python run.py reverse &lt;value&gt;` respectively.

## Unit Tests
From the root of the directory run the command `python -m unittest rotcipher.tests.__run_all` to execute all unit
tests.
