import scipy as sp
import numpy as np
from numpy.random import random


def coulomb_potential(d: float) -> float:
    if d == 0:
        return float("Inf")
    else:
        return sp.e / d


def random_wolke(n: int) -> list:
    array = np.zeros((n, 2))
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            array[i][j] = np.random.random()
    return array
