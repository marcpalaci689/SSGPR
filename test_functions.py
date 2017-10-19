'''
@author : Marc Palaci-Olgun
@date   : 10/19/2017
@descrition: The following script generates 1D benchmarking data sets.
'''

import numpy as np

# sinc test function
def sinc(N,noise=0.01):
    x = np.sort(np.random.uniform(-1,6,size=N)).reshape(-1,1)
    y = np.sinc(x) + np.random.normal(scale=noise,size=N).reshape(-1,1)
    return x,y

# step function test function
def step(N,noise=0.01):
    x = np.sort(np.random.uniform(-2,2,size=N)).reshape(-1,1)
    y = np.greater(x,0) + np.random.normal(scale=noise,size=N).reshape(-1,1)
    return x,y


    
