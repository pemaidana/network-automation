import sys
import time
import logging

# Enable logger
logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(message)s')
log = logging.getLogger(__name__)

# Import pyATS and the pyATS Library
from genie.testbed import load
from ats.log.utils import banner
from netmiko import ConnectHandler # Importando o módulo ConnectHandler
# Criando um bloco de dicionário representando a conexão SSH de um device
SW_ACCESS_1 = { 
    'device_type': 'cisco_ios', 
    'host':   '192.168.36.210',
    'username': 'teste',
    'password': 'teste',
    'port' : 22,          
    'secret': 'secret',     # opcional
}

net_connect = ConnectHandler(**SW_ACCESS_1)
output = net_connect.send_command('show int Ethernet0/2')
print(output)

pre_status = output['Ethernet0/2']['oper_status']
if pre_status == 'down':
    log.info("\nPASS: Interface Ethernet0/2 está DOWN\n")
else:
    log.error("\nFAIL: Interface Ethernet0/2 está UP\n")
    exit()
