import requests
session = requests.Session()
conf_name = "startup-config.conf"
#print(session.cookies.get_dict())

#response = session.get('https://accounts-ebeta.myzyxel.com/users/sign_in')
#print(session.cookies.get_dict())
def login_GUI():    
  conn = session.get('https://192.168.1.1',verify=False)
  #content = response.content.decode("utf-8")
  #print(content)

  login_data ={
    'username':'admin',
    'pwd':'12345',
    'password':'12345',
    'pwd_r':'',
    'mp_idx':'0'
  }
  login = session.post('https://192.168.1.1',data=login_data,verify=False)
  #login_response = login.content.decode("utf-8")
  #print(login_response)

def download_conf(name):
  get_file = session.get("https://192.168.1.1/cgi-bin/export-cgi?category=config&arg0="+ name,verify=False)
  data = get_file.content.decode("utf-8")
  #data = res.read().decode("utf-8")
  print(data)

# Wrtite the configuration file to a file
  f = open(name, "a")
  f.write(data)
  f.close()

login_GUI()
download_conf(conf_name)



