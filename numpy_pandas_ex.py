import sys
sys.path.insert(0, 'pythonfiles/')

import generators_fun_ex

import pandas as pd
import numpy as np
import pickle

# using jenkinsapi
from jenkinsapi.jenkins import Jenkins

p_data=[{1:'dell',2:'lenovo',3:'hp',4:'vaio'}]
df = pd.DataFrame(p_data)

n_data=['xperia','moto','nokia','oneplus']
n = np.array(n_data)

print "pandas output is...."
print df

print "numpy output is...."
print n

J = Jenkins('http://localhost:8080', username='srinivasreddyh', password='meghana3')
build_no=str(J['master'].get_last_build())[-3:]
print "Last BUILD_NUMBER :",build_no

filename = "/var/lib/jenkins/workspace/jenkins-python-test_master@tmp/%s.pkl" %build_no
with open(filename ,"wb") as f:
    pickle.dump(df,f)


