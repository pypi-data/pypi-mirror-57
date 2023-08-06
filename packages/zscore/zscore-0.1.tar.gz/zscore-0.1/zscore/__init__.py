# import statements
import statistics

import numpy as np
import pandas as pd

def ZScore(filename,col_name):
    data = pd.read_csv(filename)
    col_1 = data[col_name]
    array = np.array(col_1)

    m = statistics.mean(array)
    sd = statistics.stdev(array)

    i = 0
    for val in array:
        v = float((val - m) / sd)
        array[i] = v
        i = i + 1

    return array
