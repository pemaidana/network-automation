# O script IOS commands abaixo serve para alocar no arquivo "iosv_l2_config1"

vlan 2
int range g2/0
switchport mode access
switchport access vlan 2

int range g0/0-3
switchport trunk encapsulation dot1q
switchport mode trunk
switchport nonegotiate
switchport trunk allowed vlan 1,2

int range g1/0-1
switchport trunk encapsulation dot1q
switchport mode trunk
switchport nonegotiate
switchport trunk allowed vlan 1,2

from netmiko import ConnectHandler

iosv_l2_s1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.71',
    'username': 'thiago',
    'password': 'thiago',
}

iosv_l2_s2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.72',
    'username': 'thiago',
    'password': 'thiago',
}

iosv_l2_s3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.73',
    'username': 'thiago',
    'password': 'thiago',
}


with open('iosv_l2_config1') as f: 
    lines = f.read().splitlines()
print (lines)

# Criando uma variável para chamar as conexões SSH
all_devices = [iosv_l2_s1, iosv_l2_s2, iosv_l2_s3]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    
    # Nesse momento a conexão com o primeiro dicionário foi iniciada e com isso chamamos a função "net_connect.send_config_set", essa função envia comandos para o device, e em seguida alocamos dentro dessa função a variável "lines", dentro dessa variável está sendo alocados os comandos que deverão ser executados pela função
    output = net_connect.send_config_set(lines)
    print (output) # Printa a saída dos comandos que foram executados. 
