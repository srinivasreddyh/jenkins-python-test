import sys
sys.path.insert(0, 'pythonfiles/')

import generators_fun_ex

import pandas as pd
import numpy as np
import pickle

p_data=[{1:'dell',2:'lenovo',3:'hp',4:'vaio'}]
df = pd.DataFrame(p_data)

n_data=['xperia','moto','nokia','oneplus']
n = np.array(n_data)

print "pandas output is...."
print df

print "numpy output is...."
print n

with open("/var/lib/jenkins/workspace/jenkins-python-test_master@tmp/gen_output2.pkl","wb") as f:
	pickle.dump(df,f)


next_bn = server.get_job_info('job_name')['nextBuildNumber']
print "next_Build_Number :"
print next_bn
server.set_next_build_number('job_name', next_bn + 50)