import paramiko
import time

router_ip = "10.214.48.27"
#router_ip = "10.10.10.1"
router_username = "gsbuae"
router_password = "Qn080891"
ssh = paramiko.SSHClient()
# Load SSH host keys.
ssh.load_system_host_keys()
# Add SSH host key automatically if needed.
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# Connect to router using username/password authentication.
#ssh.connect(router_ip,username=router_username,password=router_password,look_for_keys=False )
ssh.connect(router_ip,username=router_username,password=router_password, timeout = 10)
if ssh.get_transport() is not None:
    print ("ssh is connected")

#Request an interactive shell session on this channel.
channel = ssh.invoke_shell()
#Send data to the channel 
channel.send('show interface all\n')
# Sleep 1 second
time.sleep(1)
#check whether data can be written to the channel without blocking
#send_data = channel.send_ready()
#print("Data has been sent",send_data)

#Check data is buffered and ready for reading from the channel
#recv_data = channel.recv_ready()
#print("Data ready to read: ",recv_data)


# Read the data from the channel
output=channel.recv(1000) # The output in byte. The ointer stop at n byte, then we can continue read 


print(output)
#print(output2)
channel.close()
ssh.close()

