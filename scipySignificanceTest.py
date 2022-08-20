import numpy as np
from scipy.stats import ttest_ind
from scipy.stats import kstest
from scipy.stats import describe 
from scipy.stats import skew ,kurtosis,normaltest

v = np.random.normal(size=100)
v1 = np.random.normal(size=100)
v2 = np.random.normal(size=100)
res = ttest_ind(v1,v2)
#Find if the given values v1 and v2 are from same distribution:
print(res)

# only return pvalue
res = ttest_ind(v1,v2).pvalue
print(res)

# kstest
print("kstest:")
res = kstest(v,'norm')
print(res)

# Describe 
res = describe(v)
print("describe:")
print(res)

# skew and kurtosis
print("skew:",skew(v))
print("kurtosis:",kurtosis(v))

# find data that comes from normal test
print("nomaltest:",normaltest(v))



