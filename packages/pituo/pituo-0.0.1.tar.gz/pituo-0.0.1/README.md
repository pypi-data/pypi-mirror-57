# pituo
Go-styled errors in Python.

## Installation
Using pip: `pip install -U pituo`


## Usage

Import the function `pituo` from the package:
```py
from pituo import pituo
```

### Using decorator syntax
```py
@pituo
def divide(dividend, divisor):
    """
    Return the result of the division between dividend and divisor.
    May raise a ZeroDivisionError if divisor is 0.
    """
    return dividend / divisor

quotient, err = divide(1, 0)

if err is not None:
    print(err)          # Prints "division by zero"
else:
    print(quotient)
```

### Wrapping the function
```py
def divide(dividend, divisor):
    """
    Return the result of the division between dividend and divisor.
    May raise a ZeroDivisionError if divisor is 0.
    """
    return dividend / divisor

divide = pituo(divide)

quotient, err = divide(4, 1)

if err is not None:
    print(err)
else:
    print(quotient)     # Prints 4
```

For more examples, see the `tests` folder.

## License
This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) license.