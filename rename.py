import os
job_name = os.environ.get('JOB_NAME', 'default_name')
build_number = os.environ.get('BUILD_NUMBER', 1)
new_output = "{}_{}.bin".format(job_name, build_number)

original_output="/var/lib/jenkins/workspace/jenkins-python-test_master@tmp/gen_output_os.pkl"
os.rename(original_output, new_output)	
