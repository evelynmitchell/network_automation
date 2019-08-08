#!/usr/bin/env python

#!/usr/bin/env python
 
import json
 
ssh_info={}
 
R1={'device_type':'cisco_ios',
    'username':'netman',
    'password':'netman',
    'ip':'198.51.100.10'
    }
 
R2={'device_type':'cisco_ios',
    'username':'netman',
    'password':'netman',
    'ip':'198.51.100.20'
    }
 

ssh_info['R1']=R1
ssh_info['R2']=R2
 
file_name=open("parth_sshInfo.json",'w')
json.dump(ssh_info,file_name)
file_name.close()
 
print("done")
