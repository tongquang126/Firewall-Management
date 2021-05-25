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

# Check ssh connection

#if ssh.get_transport() is not None:
#    print ("ssh is connected")

#Request an interactive shell session on this channel.
channel = ssh.invoke_shell()
#Send data to the channel 
channel.send('dir /conf/\t')
# Sleep 1 second
time.sleep(1)


# Read the data from the channel
output=channel.recv(1000) # The output in byte. The pointer stop at n byte, then we can continue read 
# Convert byte to unicode
output = output.decode("utf-8")  
# Write the output to the text file

#f = open('conf_file.txt', "a")
#f.write(output)
#f.close()

# Write the config file name into the list

conf_list = [y for y in (x.strip() for x in output.splitlines()) if y]  # Write the raw config list from string into a list, 1 output line to 1 list object
conf_list.remove('dir /conf/')   # remove command line appear in ssh output 
conf_list.remove('Router> dir /conf/')
conf_list.remove('Router> dir /conf/')

for i in range(0,len(conf_list)):
  conf_list[i] = conf_list[i].lstrip('/conf/') # remove /conf/ in ssh output to get the correct config file name



print(conf_list)

channel.close()
ssh.close()

