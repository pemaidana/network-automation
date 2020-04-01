import os
import json
from netmiko import ConnectHandler

user = os.environ.get('username')
pw = os.environ.get('password')
sec = os.environ.get('secret')

cisco_881 = { 
    'device_type': 'cisco_ios_telnet', # Declarando o módulo do tipo de IOS que estou interagindo
    'host':   '192.168.36.12',
    'username': 'teste',
    'password': 'teste',
    'secret': 'teste', #caso tenha senha para enable secret
    'port' : 23         
}


net_connect = ConnectHandler (**cisco_881)
net_connect.enable() 

try: 
    net_connect = ConnectHandler (**cisco_881)
    net_connect.enable() 

    output = net_connect.send_command('show ip int brief', use_textfsm=True)
    print(json.dumps(output, indent=2))
except Exception as e: 
    print(e)

    # retorno...

  {
    "intf": "Ethernet0/2",
    "ipaddr": "unassigned",
    "status": "administratively down",
    "proto": "down"
  },
  {
    "intf": "Ethernet0/3",
    "ipaddr": "unassigned",
    "status": "administratively down",
    "proto": "down"
  },
 
      
cisco_881 = {
    'device_type': 'cisco_ios', 
    'host':'192.168.36.12',
    'username':'teste',
    'password':'teste',
    'secret':'teste',
    'port': 22         
}

try: 
    net_connect = ConnectHandler (**cisco_881)
    interfaces = net_connect.send_command('show ip int brief', use_textfsm=True)
       
    # Definindo um atributo para a variável "interfaces"  
    for interface in interfaces:        
        if interface['status'] == 'administratively down':
             # Printar a variável "interface" junto com o parâmetro que queremos se referir na saída do comando da CLI e definir uma mensagem para representar esse print. 
             print(f"{interface['intf']} IS DOWN!")
    
except Exception as e: 
    print(e)   
                   
    # retorno...                   
                   
    Ethernet0/1 IS DOWN!
    Ethernet0/2 IS DOWN!
    Ethernet0/3 IS DOWN!               
