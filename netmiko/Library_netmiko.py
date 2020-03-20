# A library netmiko simplifica a library paramiko.
  
Para começar o embasamento da library netmiko, é preciso entendermos alguns parâmetros.

from netmiko import ConnectHandler # Importando o módulo ConnectHandler

# Criando um bloco de dicionário representando a conexão SSH de um device
cisco_881 = { # Essa classe cisco_881 se refere ao hostname no qual estou me conectando.
    'device_type': 'cisco_ios', # Declarando o módulo do tipo de IOS que estou interagindo com base nos módulos de dicionário Python.
    'host':   '10.10.10.10',
    'username': 'test',
    'password': 'password',
    'port' : 8022,          # optional, defaults to 22
    'secret': 'secret',     # optional, defaults to ''
}


# Estabelecendo uma conexão SSH baseado no bloco de dicionário acima
net_connect = ConnectHandler ( ** cisco_881)

# Executando comandos show
output = net_connect.send_command('show ip int brief')
print(output)

# Verificando a saída do comando
Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0              unassigned      YES unset  down                  down
FastEthernet1              unassigned      YES unset  down                  down
FastEthernet2              unassigned      YES unset  down                  down
FastEthernet3              unassigned      YES unset  down                  down
FastEthernet4              10.10.10.10     YES manual up                    up
Vlan1                      unassigned      YES unset  down                  down


# Executando comandos de configuração (entrará automaticamente no modo de configuração do device)
config_commands = [ 'logging buffered 20000',
                    'logging buffered 20010',
                    'no logging console' ]
output = net_connect.send_config_set(config_commands)
print(output)

# Verificando a saída do comando via simução de CLI
pynet-rtr1#config term
Enter configuration commands, one per line.  End with CNTL/Z.
pynet-rtr1(config)#logging buffered 20000
pynet-rtr1(config)#logging buffered 20010
pynet-rtr1(config)#no logging console
pynet-rtr1(config)#end
pynet-rtr1#

# Vale ressaltar que a simulação do script pode ser feita via aplicação jupyter, isso ajuda a entender se o script vai ser executado da maneira que queremos.



# Módulos de dicionário python que são suportados como device_types da library netmiko

CLASS_MAPPER_BASE = {
    "a10": A10SSH,
    "accedian": AccedianSSH,
    "alcatel_aos": AlcatelAosSSH,
    "alcatel_sros": NokiaSrosSSH,
    "apresia_aeos": ApresiaAeosSSH,
    "arista_eos": AristaSSH,
    "aruba_os": ArubaSSH,
    "avaya_ers": ExtremeErsSSH,
    "avaya_vsp": ExtremeVspSSH,
    "brocade_fastiron": RuckusFastironSSH,
    "brocade_netiron": ExtremeNetironSSH,
    "brocade_nos": ExtremeNosSSH,
    "brocade_vdx": ExtremeNosSSH,
    "brocade_vyos": VyOSSSH,
    "checkpoint_gaia": CheckPointGaiaSSH,
    "calix_b6": CalixB6SSH,
    "ciena_saos": CienaSaosSSH,
    "cisco_asa": CiscoAsaSSH,
    "cisco_ios": CiscoIosSSH,
    "cisco_nxos": CiscoNxosSSH,
    "cisco_s300": CiscoS300SSH,
    "cisco_tp": CiscoTpTcCeSSH,
    "cisco_wlc": CiscoWlcSSH,
    "cisco_xe": CiscoIosSSH,
    "cisco_xr": CiscoXrSSH,
    "cloudgenix_ion": CloudGenixIonSSH,
    "coriant": CoriantSSH,
    "dell_dnos9": DellForce10SSH,
    "dell_force10": DellForce10SSH,
    "dell_os6": DellDNOS6SSH,
    "dell_os9": DellForce10SSH,
    "dell_os10": DellOS10SSH,
    "dell_powerconnect": DellPowerConnectSSH,
    "dell_isilon": DellIsilonSSH,
    "endace": EndaceSSH,
    "eltex": EltexSSH,
    "eltex_esr": EltexEsrSSH,
    "enterasys": EnterasysSSH,
    "extreme": ExtremeExosSSH,
    "extreme_ers": ExtremeErsSSH,
    "extreme_exos": ExtremeExosSSH,
    "extreme_netiron": ExtremeNetironSSH,
    "extreme_nos": ExtremeNosSSH,
    "extreme_slx": ExtremeSlxSSH,
    "extreme_vdx": ExtremeNosSSH,
    "extreme_vsp": ExtremeVspSSH,
    "extreme_wing": ExtremeWingSSH,
    "f5_ltm": F5TmshSSH,
    "f5_tmsh": F5TmshSSH,
    "f5_linux": F5LinuxSSH,
    "flexvnf": FlexvnfSSH,
    "fortinet": FortinetSSH,
    "generic_termserver": TerminalServerSSH,
    "hp_comware": HPComwareSSH,
    "hp_procurve": HPProcurveSSH,
    "huawei": HuaweiSSH,
    "huawei_vrpv8": HuaweiVrpv8SSH,
    "ipinfusion_ocnos": IpInfusionOcNOSSSH,
    "juniper": JuniperSSH,
    "juniper_junos": JuniperSSH,
    "juniper_screenos": JuniperScreenOsSSH,
    "keymile": KeymileSSH,
    "keymile_nos": KeymileNOSSSH,
    "linux": LinuxSSH,
    "mikrotik_routeros": MikrotikRouterOsSSH,
    "mikrotik_switchos": MikrotikSwitchOsSSH,
    "mellanox": MellanoxMlnxosSSH,
    "mellanox_mlnxos": MellanoxMlnxosSSH,
    "mrv_lx": MrvLxSSH,
    "mrv_optiswitch": MrvOptiswitchSSH,
    "netapp_cdot": NetAppcDotSSH,
    "netscaler": NetscalerSSH,
    "nokia_sros": NokiaSrosSSH,
    "oneaccess_oneos": OneaccessOneOSSSH,
    "ovs_linux": OvsLinuxSSH,
    "paloalto_panos": PaloAltoPanosSSH,
    "pluribus": PluribusSSH,
    "quanta_mesh": QuantaMeshSSH,
    "rad_etx": RadETXSSH,
    "ruckus_fastiron": RuckusFastironSSH,
    "ruijie_os": RuijieOSSSH,
    "ubiquiti_edge": UbiquitiEdgeSSH,
    "ubiquiti_edgeswitch": UbiquitiEdgeSSH,
    "vyatta_vyos": VyOSSSH,
    "vyos": VyOSSSH,
}


