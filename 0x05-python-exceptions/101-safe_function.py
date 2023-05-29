#!/usr/bin/python3
def safe_function(fct, *args):
    import sys

    try:
        result = fct(*args)
        return (result)

    except Exception as err:
        sys.stderr.write("Exception: ")
        sys.stderr.write(str(err))
        sys.stderr.write("\n")
        return (None)
