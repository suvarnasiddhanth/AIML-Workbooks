
import sys
from dataclasses import dataclass
from typing import Self
import math
import random

"""
A custom vector class implementation for educational purposes.
"""

@dataclass(frozen=True)
class Vec:
    elements: tuple[int | float, ...] = ()
    def __init__(self, src=None) -> Self:
        if src is None:
            self.elements = ()
        else:
            elements = tuple(src)
            for x in elements:
                if not isinstance(x, (int, float)):
                    raise TypeError(f"Scalar must be a number: {type(x)}")
            self.elements = elements
        object.__setattr__(self, "elements", elements)

    def __add__(self, t: Self) -> Self:
        if not isinstance(t, Vec):
            raise TypeError(f"Expected Vec: {type(t)}")
        if len(self.elements) != len(t):
            raise TypeError(f"Type error - vectors must be of same dimensions")
        return Vec([round(x + y, 5) for x, y in zip(self.elements, t.elements)])


    def __rmul__(self, scalar: int | float) -> Self:
        if not isinstance(scalar, (int, float)):
            raise TypeError(f"Vector multiplication with invalid type: {type(scalar)}")
        return Vec([round(x * scalar, 5) for x in self.elements])

    def __imul__(self, scalar: int | float) -> Self:
        #Tuples cannot be inplace multiplied so function just returns another value, assignment will simply overwrite
        if not isinstance(scalar, (int, float)):
            raise TypeError(f"Vector multiplication with invalid type: {type(scalar)}")
        return Vec(round(x * scalar, 5) for x in self.elements)

    def mean(self) -> int | float:
        #Return the arithmetic mean of the vector entries.
        if not self.elements:
            raise ValueError("Vector is blank")
        return sum(self.elements) / len(self.elements)

    def demean(self) -> Self:
        #Return a new vector whose entries have the original vector's mean subtracted from them.
        mean = self.mean()
        return Vec(round(x - mean, 5) for x in self.elements) if mean else None

    def std(self) -> float:
        #Return the standard deviation.
        demeaned = self.demean()
        squared_deviations = [ deviation ** 2 for deviation in demeaned.elements ]
        return math.sqrt(sum(squared_deviations) / len(squared_deviations))

    def __repr__(self) -> str:
        return repr(self.elements)

    def __len__(self) -> int:
        return len(self.elements)

    def __sub__(self, t: Self) -> Self:
        if not isinstance(t, Vec):
            raise TypeError(f"Expected Vec: {type(t)}")
        if len(self.elements) != len(t.elements):
            raise TypeError("Type error - vectors must be of same dimensions")
        return Vec(round(x - y, 5)for x, y in zip(self.elements, t.elements))

    def __neg__(self) -> Self:
        return Vec(round(-x, 5) for x in self.elements)

    def __radd__(self, other):
        if isinstance(other, (int, float)) and other == 0:
            return self
        if not isinstance(other, Vec):
            raise TypeError(f"Expected Vec: {type(other)}")
        return other + self

    def __iadd__(self, other):
        # Vec is immutable, so return a new vector.
        return self + other


    # return a vector of @n zeroes. precondition: @n > 0
    @staticmethod
    def zeros(vecsize: int) -> Self:
        if not isinstance(vecsize, int):
            raise TypeError("Value must be an integer")
        if vecsize <= 0:
            raise ValueError("Value must be greater than 0")
        return Vec(0 for _ in range(vecsize))

    # return a vector of @n. precondition: @n > 0
    @staticmethod
    def ones(vecsize: int) -> Self:
        if not isinstance(vecsize, int):
            raise TypeError("Value must be an integer")
        if vecsize <= 0:
            raise ValueError("Value must be greater than 0")

        return Vec(1 for _ in range(vecsize))

    # return a vector of @n uniformly distributed numbers in [0, 1]. precondition: @n > 0
    @staticmethod
    def uniform(vecsize: int) -> Self:
        if not isinstance(vecsize, int):
            raise TypeError("n must be an integer")
        if vecsize <= 0:
            raise ValueError("n must be greater than 0")
        return Vec(random.uniform(0, 1) for _ in range(vecsize))

    # Calculates the Euclidean norm (L2 norm) of the vector.
    # sqrt(e[0]^2 + e[1]^2 + e[2]^2 + ... + e[n-1]^2)
    def norm(self) -> float:
        return math.sqrt(sum(x ** 2 for x in self.elements))


"""
(1) Understand the basic design of the vector abstraction. Review the implementation.
(2) Document each function.
(3) Implement all unimplemented methods.
(4) Create appropriate tests for this implementation, increasing the confidence about its correctness.
(5) Test this implementation by importing the class in a sepatate python script.

(6) Measure the performance of each of these functions on vectors of varying lengths.
    Try 2k to 64k dimension vectors and time the results.
    How would you do the measurements?
(7) Measure the performance on your machine. Check it on colab.

(8) use numpy and compare the performance.
"""


if sys.version_info < (3, 8):
    sys.exit("Error: This script requires Python 3.8 or higher.")

if __name__ == "__main__":
    #z1 = Vec.zeros(10)
    v1 = Vec([0, 1, 1.03])
    print(v1)
    v3 = 2.2 * v1
    v3 *= 5
    # v3 = 1 + v3
    print(v3)
    v2 = v1 + v3
    print(v1 + v3)
    #print(-(v1 + v3))

