# Sermos Utils

Utilities for interacting with Sermos.

## Testing

To run the tests you need to have `pyenv` running on your system and `tox` in
your environment.

Refer to RhoAI documentation for instructions on installing `pyenv` correctly.

After `pyenv` is intalled, then install `tox`

    $ pip install tox

Then install the different python versions in `pyenv`

    $ pyenv install 2.7.8 3.3.6 3.4.4 3.5.1

Now, run the tests:

    $ tox
