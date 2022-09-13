from setuptools import setup

if __name__ == '__main__':
    setup(
        name='rotcipher',
        version='1.0',
        description='A POC implementation of a rotation cipher',
        author='Andrew Cumming',
        author_email='andrew.e.cumming@gmail.com',
        url='https://github.com/AndrewEC/py-rot-cipher',
        packages=['rotcipher', 'rotcipher.lib']
    )
