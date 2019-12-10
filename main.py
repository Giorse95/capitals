#! /usr/bin/env python3

'''In the main.py we are importing the module check from mypackage'''

from NewPackage import capitals

import argparse


def parse_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument('name', help ='Please, insert the capital or the state')
    parser.add_argument('-v', '--verbosity',
    help = 'Incrementally increase the verbosity', action='count', default=0)
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_arguments()
    capitals.check_capital(args)
    capitals.check_state(args)







