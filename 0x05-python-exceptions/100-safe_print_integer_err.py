#!/usr/bin/python3
def safe_print_integer_err(value):
    """
    prints an integer
    prints the error in stderr
    """
    import sys

    try:
        print("{:d}".format(value))
        return (True)

    except Exception as err:
        sys.stderr.write("Exception: ")
        sys.stderr.write(str(err))
        sys.stderr.write("\n")
        return (False)
