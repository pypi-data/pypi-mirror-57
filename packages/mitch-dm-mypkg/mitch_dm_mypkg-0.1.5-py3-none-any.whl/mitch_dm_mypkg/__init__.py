__version__ = '0.1.5'

#import run

import cowsay
import sys


def main():
    cowsay.milk(sys.argv[1])


if __name__ == '__main__':
    main()
