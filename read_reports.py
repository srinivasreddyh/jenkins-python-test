import pickle
# using jenkinsapi
from jenkinsapi.jenkins import Jenkins

J = Jenkins('http://localhost:8080', username='srinivasreddyh', password='meghana3')
build_no=str(J['master'].get_last_build())[-3:]
print "Last BUILD_NUMBER :",build_no

# to read pickle file of current build
filename = "/var/lib/jenkins/workspace/jenkins-python-test_master@tmp/%s.pkl" %build_no
with open(filename ,"rb") as f2:
    new_data=pickle.load(f2)
print new_data

last_build_no=str(J['master'].get_last_good_build())[-3:]
print "Previous BUILD_NUMBER :",last_build_no
print "Last BUILD_NUMBER :",build_no