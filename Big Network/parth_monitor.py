#!/usr/bin/env python

import subprocess
import json
from prettytable import PrettyTable
import smtplib
import time

#getting the required router parameters from file
filename="parth_sshInfo.json"
a=open(filename)
b=json.load(a)
parameters={}

while(1):
	for i in list(b.keys()):
		router={}
		try:	
			#sending the SNMP request to get the uptime of the router
			temp1=subprocess.Popen(["snmpget","-v","1","-c","public",b[i]['ip'],"1.3.6.1.2.1.1.3.0"],stdout=subprocess.PIPE)
			op1=temp1.communicate()[0]
			final_op1=op1.split()
			uptime2=final_op1[4]

			int_name=["1.3.6.1.2.1.31.1.1.1.1.1","1.3.6.1.2.1.31.1.1.1.1.2","1.3.6.1.2.1.31.1.1.1.1.3","1.3.6.1.2.1.31.1.1.1.1.4","1.3.6.1.2.1.31.1.1.1.1.5"]
			int_status=["1.3.6.1.2.1.2.2.1.7.1","1.3.6.1.2.1.2.2.1.7.2","1.3.6.1.2.1.2.2.1.7.3","1.3.6.1.2.1.2.2.1.7.4","1.3.6.1.2.1.2.2.1.7.5"]
			status={}
			name_temp={}
			#sending SNMP request to get the interface status of the router
			for j in range(0,5):
				temp2=subprocess.Popen(["snmpget","-v","1","-c","public",b[i]['ip'],int_status[j]],stdout=subprocess.PIPE)
				op2=temp2.communicate()[0]
				final_op2=op2.split()
				status_temp=final_op2[3]
				if str(status_temp)!="1":
					status[j]="Down"
				else:
					status[j]="Up"
		
				temp3=subprocess.Popen(["snmpget","-v","1","-c","public",b[i]['ip'],int_name[j]],stdout=subprocess.PIPE)
				op3=temp3.communicate()[0]
				final_op3=op3.split()
				name_temp[j]=final_op3[3]

			#sending the SNMP request to get the current utilization of the router
                	temp4=subprocess.Popen(["snmpget","-v","1","-c","public",b[i]['ip'],"1.3.6.1.4.1.9.2.1.56.0"],stdout=subprocess.PIPE)
			op4=temp4.communicate()[0]
			final_op4=op4.split()
			utilization=final_op4[3]
			
		#if managment interface is down
		except:
			uptime2="unknown"
			for j in range(0,5):
				status[j]="unknown"
				name[j]="unknown"
			status[4]="Down"

		router["uptime"]=uptime2
		router["name"]=name_temp
		router["status"]=status
		router["utilization"]=utilization

		parameters[i]=router

	#printing the collected data in table
	table=PrettyTable(["Router","Uptime","Fa0/0","Fa0/1","Fa1/0","Fa1/1","Managment","CPU Utilization"])

	for i in list(b.keys()):
		table.add_row((i,str(parameters[i]["uptime"]),parameters[i]["status"][0],parameters[i]["status"][1],parameters[i]["status"][2],parameters[i]["status"][3],parameters[i]["status"][4],str(parameters[i]["utilization"])+"%"))
	print(table)
	#time.sleep(5)
	break
