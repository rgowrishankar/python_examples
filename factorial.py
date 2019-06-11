import logging

LOG = logging.getLogger(__name__)


def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)


def main():
    try:
        x = int(input("Enter the value for finding factorial:"))
    except:
        print("Please enter a number")
        return

    print("factorial(%d)= %d" % (x, fact(x)))


if __name__ == '__main__':
    main()
