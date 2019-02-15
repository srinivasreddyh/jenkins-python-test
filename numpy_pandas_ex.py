import pandas as pd
#import numpy as np

p_data=[{1:'dell',2:'lenovo',3:'hp',4:'vaio'}]
df = pd.DataFrame(p_data)

n_data=['xperia','moto','nokia','oneplus']
n = np.array(n_data)

print "pandas output is...."
print df

print "numpy output is...."
print n
