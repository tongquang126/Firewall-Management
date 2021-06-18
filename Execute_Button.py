import sys
import os
# jenkins exposes the workspace directory through env.
#sys.path.append(os.environ['/var/lib/jenkins/workspace'])
sys.path.append("/var/lib/jenkins/workspace")
import paramiko
import time
from tkinter import *
from tkinter import ttk

root = Tk()

global hostIP, hostPort, username, password
global ssh


def save_parameter():
    global hostIP,hostPort, username, password
    hostIP= host_entry.get()
    hostPort = port_entry.get()
    username= username_entry.get()
    password = password_entry.get()    
 
    print(hostIP, hostPort, username, password)
    return 0

def quit():
    import sys; sys.exit()

def connect_ssh ():
    global hostIP, hostPort, username, password, ssh
    hostIP= host_entry.get()
    hostPort = port_entry.get()
    username= username_entry.get()
    password = password_entry.get()

    ssh = paramiko.SSHClient()
    # Load SSH host keys.
    ssh.load_system_host_keys()
    # Add SSH host key automatically if needed.
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # Connect to router using username/password authentication.
    #ssh.connect(router_ip,username=router_username,password=router_password,look_for_keys=False )
    ssh.connect(hostIP,username=username,password=password, timeout = 10)
    if ssh.get_transport() is not None:
        print ("ssh is connected")

   
    #ssh.close()
def disconnect_ssh ():
    global ssh
    ssh.close()
    if ssh.get_transport() is None:
        print ("ssh is disconnected")

def apply_config ():
    global ssh
    config_file_name = config_file.get()
    #cli = "apply /conf/" + config_file_name    
    #cli_test = "show mac\n"
    #Request an interactive shell session on this channel.
    channel = ssh.invoke_shell()
    #Send data to the channel 
    channel.send("show mac\n")
    #channel.send(cli_test+"\n")
    #channel.send(cli_test)
    # Read the data from the channel
    time.sleep(1)
    output=channel.recv(1000) # The output in byte. The ointer stop at n byte, then we can continue read 
    print(output)
    channel.close()


# Telnet Connection Function 
root.title("Zyxel SSH Configuration")
root.config(bg="gray80")
#root.geometry("800x4000")

#---------------------Create a frame of SSH connection---------------------

# Create a frame for Telnet block
frameTelnet = Frame(root,width = 400, height = 215, bg="gray80", highlightbackground = "gray36",highlightthickness =0.5)
frameTelnet.grid(row=0,column =0, padx = 10, pady =10)
frameTelnet.grid_propagate(0)


# Row 1
host_label = Label(frameTelnet,text = "Host Name (or IP address)")
host_label.grid(row=0, column = 0,sticky=W,padx=10, pady = 0)
#space1 = Label(frameTelnet,text = "                         ")
#space1.grid(row=0, column = 1, padx=10, pady = 20)
port_label = Label(frameTelnet,text = "Port")
port_label.grid(row=0, column = 1,padx=10,sticky=W)

#Row 2
host_entry = Entry(frameTelnet,width=20)
host_entry.grid(row=1,column=0,sticky=W,padx=10)
#hostIP= host_entry.get()

portValue = StringVar()
portValue.set("23")
port_entry = Entry(frameTelnet,textvariable = portValue,width=5)
port_entry.grid(row=1, column = 1,sticky=W,padx=10)
#hostPort = port_entry.get()

#Row 3
username_label = Label(frameTelnet,text = "Login Name")
username_label.grid(row=2, column = 0,sticky=W,padx=10, pady = 0)
password_label = Label(frameTelnet,text = "Password")
password_label.grid(row=2, column = 1,padx=10,sticky=W)

#Row 4
username_entry = Entry(frameTelnet,width=20)
username_entry.grid(row=3,column=0,sticky=W,padx=10)
#username= username_entry.get()

password_entry = Entry(frameTelnet,width=10)
password_entry.grid(row=3,column=1,sticky=W,padx=10)
#password= password_entry.get()


# Row 5
connectType = Label(frameTelnet,text="Connection Type")
connectType.grid(row=4,column=0,sticky=W,padx=10,pady=10)

# Row 6
connectValue = IntVar()
R1=Radiobutton(frameTelnet,text="SSH",variable=connectValue,value=0)
R1.grid(row=5,column=0,sticky=W,padx=10)
#R1=Radiobutton(frameTelnet,text="Serial",variable=connectValue,value=0)
#R1.grid(row=5,column=0,sticky=W,padx=100)

# Row 7: Add Connect Button 
#Connect = Button(frameTelnet,text="Save",command = save_parameter, width =10)
#Connect.grid(row=6,column=0,padx=0,pady=10)

Connect = ttk.Button(frameTelnet,width=10,text ="Connect",command = connect_ssh)
Connect.grid( row = 6,column = 0,sticky=W,padx = 25,pady=10)

Disconnect = ttk.Button(frameTelnet,width=10,text ="Disconnect",command = disconnect_ssh)
Disconnect.grid( row = 6,column = 1,padx=0,pady=0)

# Call the function to save the SSH connection settings



#---------------------Create a frame of Configuration Upload/Download ---------------------

frameConfig = Frame(root,width = 400, height = 250, bg="gray80", highlightbackground = "gray36",highlightthickness =0.5)
frameConfig.grid(row=1,column =0, padx = 0, pady =5)
frameConfig.grid_propagate(0)
# Row 1
#Create Configuration file label
config_label = Label(frameConfig,text = "Configuration Files: ")
config_label.grid(row=1, column = 1,padx=10, pady = 10)

# Create combobox 
file_num= StringVar()
config_file = ttk.Combobox(frameConfig,width = 20, textvariable = file_num)

# add combobox drop list
config_file["value"]= ("startup-config.conf","startup-config-bad.conf","lastgood.conf","system-default.conf")
config_file.grid(row = 1, column = 2)
config_file.current()

#Row 2

# Add Download botton

download = ttk.Button(frameConfig,width=10,text ="Download",command = quit)
download.grid( row = 2,column = 1,padx=0,pady=0)

# Add a Apply bottom to apply device's existing config file
print(config_file.current())
apply = ttk.Button(frameConfig,width=10,text ="Apply",command = apply_config)
apply.grid( row = 2,column = 2,padx=0,pady=0)



# Row 3
#Create Upload file label
upload_label = Label(frameConfig,text = "Upload Config File")
upload_label.grid(row=4,column =1,padx=10,pady=10)

# Create a path 
pathValue = StringVar()
pathValue.set("         ")
path_entry = Entry(frameConfig,textvariable = pathValue,width=20)
path_entry.grid(row=4, column = 2)

#Row 4
# Add a Browser bottom 

browser = ttk.Button(frameConfig,width=10,text ="Browser",command = quit)
browser.grid( row = 5,column = 1,padx=0,pady=0)

# Add Apply botton to apply customized config

apply1 = ttk.Button(frameConfig,width=10,text ="Apply",command = quit)
apply1.grid( row = 5,column = 2,padx=0,pady=0)

root.mainloop()
connect_ssh()

#frameTelnet.update()
#print(frameTelnet.winfo_width())
#print(frameTelnet.winfo_height())
