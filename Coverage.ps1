coverage run --omit=./rotcipher/tests/* --source=rotcipher.lib --branch --module rotcipher.tests.__run_all
coverage html
./htmlcov/index.html