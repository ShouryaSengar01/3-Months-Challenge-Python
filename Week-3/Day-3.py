#NOTES
# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
# ░░     ⭐ DEAFAULT ARGUMENTSS ⭐     ░░  => A Default value for certain parameters, Default is used when that argument is omitted
# ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░     Make your Functions more flexible, reduxe # of arguments
#                                              1. Positional  2.Default 3.Keyword 4. Arbitary

#def price(money, dis = 50, tax = 0.18)
def net_price(price, discount, tax):
    return price * (1 - discount) * (1 + tax)

net_price(500, 0.1, 0.18)

#-------------------------------------------------------------------------

import time
from termcolor import colored

def timer(end, start = 0):
    for _ in range(start, end+1):
        print(_)
        time.sleep(1)
    print(colored("DONE!!", "green"))

timer(3)
