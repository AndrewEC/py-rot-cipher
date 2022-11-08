Usage
=====

.. toctree::
   :maxdepth: 4


Run the powershell script **CreateVenv.ps1** to create a testbed which will create a virtual environment, install the
required Click dependency as well as the rotcipher package itself.

After installation, you can apply and reverse the rotational cipher on a string using::

    python run.py apply string_to_encode

and::

    python run.py reverse string_to_decode

respectively.

Additionally, you can apply and reverse a versioned rotational cipher on a string using::

    python run.py apply-versioned A string_to_encode

and::

    python run.py reverse-versioned string_to_decode

respectively.