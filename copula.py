#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
import math
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from statistics import NormalDist


rv = np.random.uniform(0, 1, 10000)
rho = 0.8
type(rv)



vecfunc = np.vectorize(NormalDist(mu=0, sigma=1).inv_cdf)
norm_rv_array_1d = vecfunc(rv)

norm_rv_array_2d = np.reshape(norm_rv_array_1d, (-1, 2))

norm_rv_df = pd.DataFrame(norm_rv_array_2d, columns=['V1', 'V2'])



# X1 = norm_rv_df.iloc[:,[0]]
# X2 = rho * norm_rv_df.iloc[:,[0]] + (1 - rho**2)**0.5 * norm_rv_df.iloc[:,[1]]

X1 = norm_rv_df['V1']
X2 = rho * norm_rv_df['V1'] + math.sqrt(1 - rho**2) * norm_rv_df['V2']

vectors = [X1, X2]

result = pd.concat(vectors)

print(result)

np.cov(X1, X2)[0][1]
np.var(X1)



plt.plot(X1, X2, 'r')
            



