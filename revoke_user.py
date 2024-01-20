from sys import stdin,stdout,stderr
from ipaddress import ip_address
import paramiko, time

ipAddress = [
    "192.168.88.1"
]

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)

users = [
    "syahid",
    "bewok"
]

for ip in ipAddress:
    try:
        ssh.connect(hostname=ip, username="admintest", password="rahasia", timeout=5)
        print("SSH connection succesful on IP" +ip)
        time.sleep(2)
        stdin,stdout,stderr = ssh.exec_command("user print")
        print (stdout.read().decode("ascii").strip("\n"))
        
        for user in users:
            ssh.exec_command("user remove [find name="+user+"]")
            print("Success Delete User "+user+"\n")
            time.sleep(2)
            stdin,stdout,stderr = ssh.exec_command("user print")
            print (stdout.read().decode("ascii").strip("\n"))
    except TimeoutError as e:
        print(f"Error: {e} connection on IP "+ip)
    finally:
        ssh.close()