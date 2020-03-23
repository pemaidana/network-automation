import os
import json
from netmiko import ConnectHandler

user = os.environ.get('username')
pw = os.environ.get('password')
sec = os.environ.get('secret')

cisco_881 = { # Essa classe cisco_881 se refere ao hostname no qual estou me conectando.
    'device_type': 'cisco_ios_telnet', # Declarando o módulo do tipo de IOS que estou interagindo com base nos módulos de dicionário Python que faz parte da library netmiko.
    'host':   '192.168.36.12',
    'username': 'teste',
    'password': 'teste',
    'secret': 'teste', #caso tenha senha para enable secret
    'port' : 23         
}



# Estabelecendo uma conexão SSH baseado no bloco de dicionário acima
net_connect = ConnectHandler (**cisco_881)
net_connect.enable() 

# Executando comandos show
output = net_connect.send_command('show ip int brief')
print((output)

# ou

try: #serve para abrir um bloco e alocar parâmetros dentro desse bloco para determinadas configurações
    net_connect = ConnectHandler (**cisco_881)
    net_connect.enable() 

    output = net_connect.send_command('show ip int brief', use_textfsm=True)
    print(json.dumps(output, indent=2))
except Exception as e: #  fecha o bloco 
    print(e)

    # Para esse script o conceito de bloco funcionária sem o "try"

    # Ao executar o script, tivemos o seguinte retorno...

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
 
      

      
# Analisando outro script
      
import os
import json
from netmiko import ConnectHandler

user = os.environ.get('username')
pw = os.environ.get('password')
sec = os.environ.get('secret')

cisco_881 = { # Essa classe cisco_881 se refere ao hostname no qual estou me conectando.
    'device_type': 'cisco_ios_telnet', # Declarando o módulo do tipo de IOS que estou interagindo com base nos módulos de dicionário Python que faz parte da library netmiko.
    'host':'192.168.36.12',
    'username':'teste',
    'password':'teste',
    'secret':'teste', #caso tenha senha para enable secret
    'port': 23         
}

# Analizando outros parâmetros
try: 
    net_connect = ConnectHandler (**cisco_881)
    net_connect.enable() 

    interfaces = net_connect.send_command('show ip int brief', use_textfsm=True)
    #print(json.dumps(output, indent=2))
    
    # Definindo um atributo para a variável "interfaces"  
    for interface in interfaces:
        # Aqui é definido que, se o o parâmetro "status" (tirado da saída JSON) estiver com o valor "administratively down"...
        if interface['status'] == 'administratively down':
             # Printar a variável "interface" junto com o parâmetro que queremos se referir na saída do comando da CLI e definir uma mensagem para representar esse print. 
             print(f"{interface['intf']} IS DOWN!")
    
except Exception as e: 
    print(e)
      
                   
    # Ao executar o script, tivemos o seguinte retorno...                   
                   
    Ethernet0/1 IS DOWN!
    Ethernet0/2 IS DOWN!
    Ethernet0/3 IS DOWN!               
