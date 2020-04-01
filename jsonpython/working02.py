import os
import json
from netmiko import ConnectHandler

user = os.environ.get('username')
pw = os.environ.get('password')
sec = os.environ.get('secret')

cisco_881 = {
    'device_type': 'cisco_ios_telnet',
    'host':   '192.168.36.12',
    'username': 'teste',
    'password': 'teste',
    'secret': 'teste', 
    'port' : 23         
}

try: 
    net_connect = ConnectHandler (**cisco_881)
    net_connect.enable() 

    stps = net_connect.send_command('show spanning-tree', use_textfsm=True)
    print(json.dumps(stps, indent=2))
except Exception as e: 
    print(e)

    # retorno...
  [
  {
    "vlan_id": "1",
    "interface": "Et0/0",
    "role": "Desg",
    "status": "FWD",
    "cost": "100",
    "port_priority": "128",
    "port_id": "1",
    "type": "P2p "
  },
  {
    "vlan_id": "1",
    "interface": "Et0/1",
    "role": "Desg",
    "status": "LRN",
    "cost": "100",
    "port_priority": "128",
    "port_id": "2",
    "type": "P2p "
  },
  {
    "vlan_id": "1",
    "interface": "Et0/2",
    "role": "Desg",
    "status": "LRN",
    "cost": "100",
    "port_priority": "128",
    "port_id": "3",
    "type": "P2p "
  },
  {
    "vlan_id": "1",
    "interface": "Et0/3",
    "role": "Desg",
    "status": "LRN",
    "cost": "100",
    "port_priority": "128",
    "port_id": "4",
    "type": "P2p "
  }
]

# Analisando outro script

cisco_881 = {
    'device_type': 'cisco_ios_telnet', 
    'host':'192.168.36.12',
    'username':'teste',
    'password':'teste',
    'secret':'teste', 
    'port': 23         
}

try: 
    net_connect = ConnectHandler (**cisco_881)
    net_connect.enable() 

    stps = net_connect.send_command('show spanning-tree', use_textfsm=True)
    print(json.dumps(stps, indent=2))
    for stp in stps:
        print(' ') # Espaçamento das linhas
        # printando os parâmetros da saída da CLI. queremos definir a vlan que a interface pertence e se a interface está em modo de designated.
        print(f"{stp['interface']}.{stp['vlan_id']} is currently in role {stp['role']} ")
    
except Exception as e: 
    print(e)
    
    
    # Ao executar o script, tivemos o seguinte retorno...  
     
    Et0/0.1 is currently in role Desg 

    Et0/1.1 is currently in role Desg 

    Et0/2.1 is currently in role Desg 

    Et0/3.1 is currently in role Desg 
    
 # OBS: Essa forma de automação se encaixaria muito em um ambiente de operação onde você deve executar shows nos device
 # e fazer com que todos retornam uma saída personalizada e com isso montar uma documentação.
