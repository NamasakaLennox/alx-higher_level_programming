#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    import calculator_1 as calc
    length = len(argv) - 1

    if (length != 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    operator = argv[2]

    if (operator == "+"):
        print("{:d} {} {:d} = {:d}".format(a, operator, b, calc.add(a, b)))
    elif (operator == "-"):
        print("{:d} {} {:d} = {:d}".format(a, operator, b, calc.sub(a, b)))
    elif (operator == "*"):
        print("{:d} {} {:d} = {:d}".format(a, operator, b, calc.mul(a, b)))
    elif (operator == "/"):
        print("{:d} {} {:d} = {:d}".format(a, operator, b, calc.div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
