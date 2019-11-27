#! /usr/bin/env python3

'''We are importing check module from NewPackage'''

from NewPackage import checks

checks.capitals.check_capital("Germany")
checks.capitals.check_capital("Honduras")
checks.capitals.check_state("Rome")
checks.capitals.check_state("Tokyo")


