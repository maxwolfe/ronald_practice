"""
This is a program that will swap two ints without a temp variable
"""


def main():
    """
    This is the main which is where the work will be done
    """
    int1 = int(input("Enter a int value for x: "))
    int2 = int(input("Enter a int value for y: "))
    int1, int2 = int2, int1
    print(int1, int2)


if __name__ == '__main__':
    main()
