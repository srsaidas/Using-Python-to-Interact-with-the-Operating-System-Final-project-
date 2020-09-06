#!/usr/bin/env python3

#importing packages
import re
import operator
import sys
import csv


#loading system log file as cml
log_file= open(sys.argv[1],"r")

#initialisation of variable  
user_static={}
error_message={}

#csv headers
user_colum_names= ['Username', 'INFO', 'ERROR']
err_colum_names=['Error','count']

#Reading file line by line
for  line in log_file.readlines():

    #Regular expresssion
    error = re.search(r"ticky: ERROR * ([\w ']*) \(([\w.]*)\)",line)
    info = re.search(r"ticky: INFO [\w \[\]#]* \(([\w.]*)\)",line)

    if error:
        error_message[error.group(1)] = error_message.get(error.group(1),0)+1
        user_static[error.group(2)] = [user_static.get(error.group(2),[0,0])[0],user_static.get(error.group(2),[0,0])[1]+1]
    
    if info:
        user_static[info.group(1)] = [user_static.get(info.group(1),[0,0])[0]+1,user_static.get(info.group(1),[0,0])[1]]


with open('error_message.csv ','w') as out:
    csv_out=csv.writer(out)
    csv_out.writerow(err_colum_names)
    csv_out.writerows(sorted(error_message.items(), key=operator.itemgetter(1), reverse=True))


with open('user_statistics.csv','w') as out:
    csv_out=csv.writer(out)
    csv_out.writerow(user_colum_names)
    for user in sorted(user_static.items()):
        csv_out.writerow([user[0],user[1][0],user[1][1]])

