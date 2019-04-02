import pandas as pd
import pickle
# using jenkinsapi
from jenkinsapi.jenkins import Jenkins

p_data=[{1:'dell',2:'lenovo',3:'hp',4:'vaio'}]
df = pd.DataFrame(p_data)

print "pandas output is...."
print df

J = Jenkins('http://localhost:8080', username='srinivas', password='wildly123')
build_no=str(J['master'].get_last_build())[-3:]
print "current BUILD_NUMBER :",build_no

# create a pickle file, buid_number as name
filename = "/var/lib/jenkins/workspace/jenkins-python-test_master@tmp/%s.pkl" %build_no
with open(filename ,"wb") as f:
    pickle.dump(df,f)