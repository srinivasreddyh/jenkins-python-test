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
build_no=str(J['master'].get_last_good_build())[-2:]
print "Current BUILD_NUMBER :",build_no

filename = "/var/lib/jenkins/workspace/jenkins-python-test_master@tmp/%s.pkl" %build_no
with open(filename ,"wb") as f:
    pickle.dump(df,f)


#with open("/var/lib/jenkins/workspace/jenkins-python-test_master@tmp/gen_output.pkl","wb") as f:
#	pickle.dump(df,f)
'''
import os
job_name = os.environ.get('JOB_NAME', 'default_name')
build_number = os.environ.get('BUILD_NUMBER', 1)
new_output = "{}_{}.bin".format(job_name, build_number)

original_output="/var/lib/jenkins/workspace/jenkins-python-test_master@tmp/gen_output_os.pkl"
os.rename(original_output, new_output)	
'''
'''
import jenkins
next_bn = server.get_job_info('job_name')['nextBuildNumber']
print "next_Build_Number :"
print next_bn
server.set_next_build_number('job_name', next_bn + 50)
'''