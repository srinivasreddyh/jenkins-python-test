import pickle 
import pandas as pd

with open("/home/srinivas/mypython/cl_report.pkl","rb") as f1:
	data1=pickle.load(f1)
#print data1

with open("/home/srinivas/mypython/cl_report2.pkl","rb") as f2:
	data2=pickle.load(f2)
#print data2

df1=pd.DataFrame(data1)
#print "\nPrevious Results :"
#print df1,"\n"

df2=pd.DataFrame(data2)
#print "\nCurrent Results :"
#print df2 ,"\n"

# dropping support
final_df1=df1.drop(['support'])
final_df2=df2.drop(['support'])
print "\nPrevious Results :\n",final_df1
#print final_df1,"\n"
print "\nCurrent Results :\n",final_df2
#print final_df2,"\n"

# columns=['Motor_Sound','Explosion_Sound','Human_Sound','Nature_Sound', \
#               'Domestic_Animals','Tools','macro_avg','micro_avg','weighted_avg']

print "\n============ Motor_Sounds =============="
motor_sound=(final_df2.loc[:,'0'] - final_df1.loc[:,'0']) *100
#print motor_sound
for key, value in motor_sound.iteritems():
    if value > 0:
        print key,"increased by", format(value).replace("-",""),"%"
    else:
        print key," decreased by", format(value).replace("-",""),"%"
        
print "\n========== Explosion_Sounds ============"
explosion_sound=(final_df2.loc[:,'1'] - final_df1.loc[:,'1']) *100
#print explosion_sound
for key, value in explosion_sound.iteritems():
    if value > 0:
        print key,"increased by", format(value).replace("-",""),"%"
    else:
        print key," decreased by", format(value).replace("-",""),"%"

print "\n============ Human_Sound =============="
human_sound=(final_df2.loc[:,'2'] - final_df1.loc[:,'2']) *100
#print human_sound
for key, value in human_sound.iteritems():
    if value > 0:
        print key,"increased by", format(value).replace("-",""),"%"
    else:
        print key," decreased by", format(value).replace("-",""),"%"

print "\n=========== Nature_Sound ============="
nature_sound=(final_df2.loc[:,'3'] - final_df1.loc[:,'3']) *100
#print nature_sound
for key, value in nature_sound.iteritems():
    if value > 0:
        print key,"increased by", format(value).replace("-",""),"%"
    else:
        print key," decreased by", format(value).replace("-",""),"%"

print "\n========== Domestic_Animals ============"
domestic_animals=(final_df2.loc[:,'4'] - final_df1.loc[:,'4']) *100
#print domestic_animals
for key, value in domestic_animals.iteritems():
    if value > 0:
        print key,"increased by", format(value).replace("-",""),"%"
    else:
        print key," decreased by", format(value).replace("-",""),"%"

print "\n=============== Tools ================="
tools=(final_df2.loc[:,'5'] - final_df1.loc[:,'5']) *100
#print tools
for key, value in tools.iteritems():
    if value > 0:
        print key,"increased by", format(value).replace("-",""),"%"
    else:
        print key," decreased by", format(value).replace("-",""),"%"

print "\n============= Macro_Avg ==============="
macro_avg=(final_df2.loc[:,'macro avg'] - final_df1.loc[:,'macro avg']) *100
#print macro_avg
for key, value in macro_avg.iteritems():
    if value > 0:
        print key,"increased by", format(value).replace("-",""),"%"
    else:
        print key," decreased by", format(value).replace("-",""),"%"

print "\n============== Micro_Avg ==============="
micro_avg=(final_df2.loc[:,'micro avg'] - final_df1.loc[:,'micro avg']) *100
#print micro_avg
for key, value in micro_avg.iteritems():
    if value > 0:
        print key,"increased by", format(value).replace("-",""),"%"
    else:
        print key," decreased by", format(value).replace("-",""),"%"

print "\n============ Weighted_Avg =============="
weighted_avg=(final_df2.loc[:,'weighted avg'] - final_df1.loc[:,'weighted avg']) *100
#print weighted_avg
for key, value in weighted_avg.iteritems():
    if value > 0:
        print key,"increased by", format(value).replace("-",""),"%"
    else:
        print key," decreased by", format(value).replace("-",""),"%"     


#from slackclient import SlackClient
#sc = SlackClient('token')

#sc.api_call("files.upload", filename='jenkins_output.txt', \
#    channels='#jenkin_slack_notifier',username='srinivas_reddy_h', \
#    file=open('/var/lib/jenkins/workspace/jenkins-python-test_master@tmp/jenkins_output.txt', 'r').read())           