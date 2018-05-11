# PyCalculator unit tests

## Requirements

You need **pytest** to launch the tests. You can install pytest the following way:

```
sudo pip install pytest
```

## Run the tests

First, you have to modify **PYTHONPATH** environment variable in order to allow python to import from parent directory:

```
export PYTHONPATH=$PYTHONPATH:..
```

Then, you're ready to start the tests. You can run all the tests:

```
pytest
```

Or just run a specific test:

```
pytest test_operator
```