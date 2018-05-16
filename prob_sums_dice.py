''' Find the probability that a roll of x number of dice will add up to n '''
from itertools import product
from decimal import *

def rolldice_sum_prob(n, dice_num):
    '''
    Find number of possible combos adding up to n in dice_num number of dice
    Return number of matches divided by the total combos to get the
    probability of a match. Apply Decimal() and float() to prevent rounding
    '''
    di = [1,2,3,4,5,6]
    dice = [di for i in range(dice_num)]
    combos = [combo for combo in product(*dice) if sum(combo) == n]
    return float(Decimal(len(combos)) / Decimal(6**dice_num))