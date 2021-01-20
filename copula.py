#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
import math
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from statistics import NormalDist



def get_copula_vectors(rv, rho=0.8):
	X1 = rv[:,0]
	X2 = rho * X1 + math.sqrt(1 - rho**2) * rv[:,1]
	return X1, X2



if __name__ == '__main__':

	rv = np.random.uniform(0, 1, 10000)

	# without vectorize function just using list comprehension
	norm_rv_df = np.asarray([NormalDist(mu=0, sigma=1).inv_cdf(i) for i in rv]).reshape(-1,2)

	# get X1 and X2
	X1,X2 = get_copula_vectors(norm_rv_df)


	#concat two numpy arrays
	result= np.concatenate((X1, X2), axis = None)


	print(result)


	np.cov(X1, X2)[0][1]
	np.var(X1)


	plt.plot(X1, X2, 'r')
	plt.show()
            



