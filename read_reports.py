import pickle
# using jenkinsapi
from jenkinsapi.jenkins import Jenkins

J = Jenkins('http://localhost:8080', username='srinivas', password='wildly123')

# to get current BUILD_NUMBER
build_no=str(J['master'].get_last_build())[-2:]
print "current BUILD_NUMBER :",build_no

# to read pickle file of current build
filename = "/var/lib/jenkins/workspace/jenkins-python-test_master@tmp/%s.pkl" %build_no
with open(filename ,"rb") as f1:
    new_data1=pickle.load(f1)
print "\ncurrent BUILD data :",new_data1

# to get previous BUILD_NUMBER
last_build_no=str(J['master'].get_last_good_build())[-3:]
print "Previous BUILD_NUMBER :",last_build_no

# to read pickle file of previous build
filename = "/var/lib/jenkins/workspace/jenkins-python-test_master@tmp/%s.pkl" %last_build_no
with open(filename ,"rb") as f2:
    new_data2=pickle.load(f2)
print "\nprevious BUILD data :",new_data2