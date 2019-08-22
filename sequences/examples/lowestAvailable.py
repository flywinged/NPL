from sequences import Sequence

import numpy

def stepSize(i: int) -> int:
    return i

def generationFunction(sequence: Sequence, i: int) -> int:

    if not hasattr(sequence, "valueSet"):
        sequence.valueSet = set()
        for j in range(i):
            sequence.valueSet.add(sequence.values[j][0])

    previousValue = sequence.values[i - 1][0]
    step = stepSize(i)

    prospectiveValue = previousValue - step

    if prospectiveValue < 0:
        sequence.valueSet.add(previousValue + step)
        return previousValue + step
    
    if prospectiveValue in sequence.valueSet:
        sequence.valueSet.add(previousValue + step)
        return previousValue + step

    return prospectiveValue