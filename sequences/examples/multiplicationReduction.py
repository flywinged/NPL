'''

'''

from sequences import Sequence

import numpy

def iterateNumber(n: int) -> int:
    '''

    '''

    nString = str(n)

    multiplication = 1

    for i in nString:
        if i != "0":
            multiplication *= int(i)
    
    return n - multiplication

def generationFunction(sequence: Sequence, i: int) -> int:
    '''

    '''

    repititions = 0
    while i > 10:
        i = iterateNumber(i)
        repititions += 1
    
    return repititions

