import os

path_to_access_log = "/var/log/apache2/access.log"
path_to_temp_log = "/tmp/access.log"

usage_threshold = 50

os.system("sudo cat "path_to_access_log" | grep \"xmlrpc.php\" > "+path_to_temp_log)

ipList = {}
for line in file(path_to_temp_log):
        line = line.strip()
        lineLst = line.split()
        ip = lineLst[0]
        if ip not in ipList:
                ipList[ip]=1
        else:
                ipList[ip]+=1

for ip in ipList:
        print ip+"\t"+str(ipList[ip])
        if ipList[ip]>usage_threshold:
                os.system("sudo iptables -A INPUT -s "+ip+" -j DROP")
