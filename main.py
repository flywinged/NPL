from sequences import Sequence
from sequences.examples import multiplicationReduction_GenerationFunction, lowestAvailable_GenerationFunction
import numpy

if __name__ == "__main__":
    
    S = Sequence(lowestAvailable_GenerationFunction, numpy.array([[0]]))

    S.generateTerms(1e4)

    print(S.values)
    S.showSequence()
