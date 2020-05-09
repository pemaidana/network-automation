# Python
import sys
import time
import logging

# Enable logger
logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(message)s')
log = logging.getLogger(__name__)

# Import pyATS and the pyATS Library
from genie.testbed import load
from ats.log.utils import banner


# ----------------
# Load the testbed
# ----------------
log.info(banner("Carregando arquivo testbed"))
testbed = load('testbed.yaml')
log.info("\nPASS: Arquivo testbed carregado com sucesso '{}'\n".format(testbed.name))


# --------------------------
# Connect to device nx-osv-1
# --------------------------
log.info(banner("Conectando no device 'SW_ACCESS_1'"))
device = testbed.devices['SW_ACCESS_1']
device.connect(via='cli')
log.info("\nPASS: Device 'SW_ACCESS_1' conectado com sucesso\n")


# ---------------------------------------
# Execute parser to check interface state
# ---------------------------------------
log.info(banner("Executando parser filtrar parâmetros..."))
pre_output = device.parse("show interface Ethernet0/2")

# Verify interface is down before unshutting
pre_status = pre_output['Ethernet0/2']['oper_status']

if pre_status == 'down':
    log.info("\nPASS: Interface Ethernet0/2 está DOWN\n")
else:
    log.error("\nFAIL: Interface Ethernet0/2 está UP\n")
    exit()


# -------------------------------------------------
# Unshut the interface by configuring "no shutdown"
# -------------------------------------------------
log.info(banner("Ligando a interface..."))
device.configure("interface Ethernet0/2\n"
                 " no shutdown")
log.info("\nPASS: Interface Ethernet0/2 está UP\n")


# -----
# Sleep
# -----
log.info("\n10 segundos para o tráfego na interface entrar em vigor...\n")
time.sleep(10)

'''
# ---------------------------------------
# Execute parser to check interface state
# ---------------------------------------
log.info(banner("Executing parser to verify interface state after unshutting..."))
post_output = device.parse("show interface Ethernet0/2")

# Verify interface is up after unshutting
post_status = post_output['Ethernet0/2']['oper_status']
if post_status == 'up':
    log.info("\nPASS: Interface Ethernet0/2 status is 'up' as expected\n")
else:
    log.error("\nPASS: Interface Ethernet0/2 status is not 'up' as expected\n")
'''