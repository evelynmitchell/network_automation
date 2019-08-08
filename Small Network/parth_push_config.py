#!/usr/bin/env python
import os
from netmiko import ConnectHandler
import json
import threading
 
def push_config(i,ssh_details,config_details):
	commands=[]
	if os.path.isfile(config_details):
		open_config=open(config_details)

		#making list of commands with each line in config file
		for line in open_config:
			if line.strip():
				commands.append(line.strip())

		#opening SSH session to router
		conn=ConnectHandler(**ssh_details)
		print("Connected to {} for configuration.".format(i))
		
		#pushing the config to router
		o1=conn.send_config_set(commands)
		print("Configuration completed on {}.".format(i))
	else:
		print("{} doesn't exists. Please check.".format(config_details))
 
if __name__=="__main__":
 
        filename="parth_sshInfo.json"
 
	#getting the SSH credentails for all routers
        a=open(filename)
        ssh_info=json.load(a)
        a.close()
 
 	#all config file names
        config_info={}
        config_info['R1']="R1_config.txt"
        config_info['R2']="R2_config.txt"


        #pushing the configs with threadding for better efficiency
        t=[]
        for i in list(config_info.keys()):
                thread=threading.Thread(target=push_config,args=(i,ssh_info[i],config_info[i]))
                thread.start()
                t.append(thread)
 
        for i in t:
                i.join()
