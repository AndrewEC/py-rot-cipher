# rot-cipher
A POC Python implementation of a rotational cipher that tries to overcome the most common pitfalls of using a
simple rotational cipher without making the implementation overly complicated.

## Cloning
To clone the project and the required submodules run:
> git clone --recurse-submodules https://github.com/AndrewEC/py-rot-cipher.git

## Usage
Run the powershell script `CreateVenv.ps1` to create a testbed which will create a virtual environment, install the
required Click dependency as well as the rotcipher package itself

After installation, you can apply and reverse the rotational cipher on a string using
`python run.py apply string_to_encode` and `python run.py reverse string_to_decode` respectively.

Additionally, you can apply and reverse a versioned rotational cipher on a string using
`python run.py apply-versioned A string_to_encode` and `python run.py reverse-versioned string_to_decode`
respectively.

## Quality Metrics
To run the unit and integration tests simply run the `CreateVenv.ps1` script the run the build script via:
`python build.py`

This build script, in addition to the running the unit and mutation tests, will also generate coverage reports,
install required dependencies, ensure a proper virtual environment is active, generate Sphinx docs, and run Flake8.

Separate mutation and unit test coverage reports will be generated at the following locations:
* Unit Tests - `html/index.html`
* Mutation Tests - `html/index.html`