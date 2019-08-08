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
 
R5={'device_type':'cisco_ios',
    'username':'netman',
    'password':'netman',
    'ip':'198.51.100.50'
    }
 
R6={'device_type':'cisco_ios',
    'username':'netman',
    'password':'netman',
    'ip':'198.51.100.60'
    }

R3={'device_type':'cisco_ios',
    'username':'netman',
    'password':'netman',
    'ip':'198.51.100.30'
    }

R4={'device_type':'cisco_ios',
    'username':'netman',
    'password':'netman',
    'ip':'198.51.100.40'
    }

ssh_info['R1']=R1
ssh_info['R2']=R2
ssh_info['R5']=R5
ssh_info['R6']=R6
ssh_info['R3']=R3
ssh_info['R4']=R4
 
file_name=open("parth_sshInfo.json",'w')
json.dump(ssh_info,file_name)
file_name.close()
 
print("done")
