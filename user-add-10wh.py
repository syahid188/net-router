import ipaddress
from sys import stderr, stdin, stdout
import paramiko

#paramiko parameters for policy & ssh client
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ipaddress_1 = "10.187.7.78"#raena


#raena
ssh.connect(hostname=ipaddress_1, port=60556, username='syahid', password='syahid#1001#')
ssh.exec_command("system script
add comment=publicip dont-require-permissions=yes name=publicip owner=admin \
    policy=read,write,test source="/tool fetch mode=https http-method=post htt\
    p-header-field=\"Content-Type: application/json\" http-data=\"{\\\"data\\\
    \": {\\\"site_code\\\": \\\"WH-TES04\\\", \\\"cat0\\\": \\\"TEST\\\", \\\"\
    cat1\\\": \\\"\\\"}}\" url=\"https://gateway.shipper.id/cicd/v1/network/ip\
    \" output=user;"")




