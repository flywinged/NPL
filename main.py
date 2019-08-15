from sequences.sequence import Sequence
import numpy

def f(sequence, i):
    return sequence[i - 1] + 1

if __name__ == "__main__":
    
    S = Sequence(f, numpy.array([[1]]))

    S.generateTerms(10)

    print(S.values)
    S.showSequence()