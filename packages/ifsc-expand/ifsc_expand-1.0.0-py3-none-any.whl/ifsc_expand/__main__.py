import argparse
from .utils import *

def main():
    parser = argparse.ArgumentParser(description='Get bank branch details from Indian Financial System Code(IFSC)')
    parser.add_argument('-i', '--ifsc', type=str, nargs=1, metavar='ifsc', default='', help='IFS Code of the branch')

    args = parser.parse_args()

    branch_details = get_branch_details(args.ifsc[0])
    print_branch_details(branch_details)


if __name__ == '__main__':
    main()