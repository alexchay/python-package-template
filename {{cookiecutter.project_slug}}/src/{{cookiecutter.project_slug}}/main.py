import os
import pprint
import sys


def main() -> None:
    """
    This is the main function of the program. It prints the current system path and the value of the 'ENVIRONMENT'
    environment variable.
    """
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(sys.path)
    print(os.environ.get("ENVIRONMENT"))


if __name__ == "__main__":
    main()
