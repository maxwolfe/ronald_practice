"""
This program will be a simple calculator (add, subtract, divide, multiply)
"""


def add(
        x: int,
        y: int,
) -> int:
    """
    This function will be the add operator

    :param x: x will act as the first addend
    :param y: y will act as the second addend
    :return int: the sum will be an integer
    """

    return x + y


def subtract(
       x: int,
       y: int,
) -> int:
    """
    This function will be the subtraction operator

    :param x will be the minuend
    :param y will be the subtrahend
    :return int: the difference will be an integer
    """

    return x - y


def divide(
        x: int,
        y: int,
) -> int:
    """
    This function will be the division operator

    :param x will be the divisor
    :param y will be the divident
    :return int: the quotient will be an int with a remainder
    """

    if y == 0:
        TypeError('Cannot Divide by 0')
    else:

    return (x / y, x % y)


def multiply(
        x: int,
        y: int,
) -> int:
    """
    This funciton will be the multiplication operator

    :param x will be a factor
    :param y will be a factor
    :return int: the quotient will be an int with a remainder
    """

    return x * y


def main():
    input_x = input(
            'Enter your first value: ',
    )

    input_y = input(
            'Enter your second value: ',
    )

    print('Possible Operators: +, -, *, /')
    operator_input = input(
            'Enter your operator: '
    )

    if operator_input == '+':
        result = add(
            input_x,
            input_y,
        )
    elif operator_input == '-':
        result = subtract(
            input_x,
            input_y,
        )
    elif operator_input == '/':
        result = divide(
            input_x,
            input_y,
        )
    elif operator_input == '*':
        result = multiply(
            input_x,
            input_y
        )
    else:
        print('enter a valid operator')

    print(result)

if __name__ == '__main__':
    main()
