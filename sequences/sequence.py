import numpy
from types import FunctionType
from typing import Tuple

import matplotlib.pyplot as plt

class Sequence:
    '''
    Base class for sequences.

    Parameters
    ----------
    generationFunction: This is the function which describes how new terms will be added to the sequence.

    initialValues: This is the numpy array which describes whatever initial conditions are required for the sequence.
    '''

    def __init__(self, generationFunction: FunctionType, initialValues: numpy.ndarray):
        
        self.generationFunction: FunctionType = generationFunction
        self.values: numpy.ndarray = initialValues
        self.newValues: numpy.ndarray = numpy.zeros((1, 1))
    
    def generateTerms(self, n: int):
        '''
        Generate terms until there are more self.values than n.

        Parameters
        ----------
        n: The number of total terms to include in the sequence.
        '''

        # Create the new shape
        newShape = numpy.zeros((len(self.values.shape),), numpy.int)
        newShape[0] = n
        newShape[1:] = numpy.array(self.values.shape)[1:]

        # Copy the old data into the newValues
        newValues = numpy.zeros(tuple(newShape))
        i = self.values.shape[0]
        newValues[:i] = self.values
        self.values = newValues

        # Create all the new values necessary and set self.values equal to the calculated new values
        while i < n:

            # Print out a return log of percentage completed
            if i % 250 == 0:
                print("Currently Generating " + str(n) + " terms: " + str(round(i / n * 100, 2)) + "%", end = "\r")

            self.values[i] = self.generationFunction(self, i)
            i += 1
    
    def showSequence(self, imgSize: Tuple[int, int] = (800, 800), savePath: str = None):
        '''
        Creates an image of a sequence.

        Parameters
        ----------
        imgSize:

        savePath:
        '''

        plt.plot(self.values, linestyle = "None", marker = "o", markersize = .02)
        plt.show()

