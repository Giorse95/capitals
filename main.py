#! /usr/bin/env python3

'''In the main.py we are importing the module check from mypackage'''

from NewPackage import capitals

import sys 

if __name__ == __main__:
	capitals.check_capital(sys.argv[1])
else:
	print("Please type a valide capital")


checks.check_capital("Germany")
checks.check_capital("Honduras")
checks.check_state("Rome")
checks.check_state("Tokyo")



