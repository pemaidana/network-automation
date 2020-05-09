# Python
import sys
import time
import logging
from unicon.core.errors import TimeoutError, StateMachineError, ConnectionError
# Import pyATS and the pyATS Library
from pyats import aetest
from genie.testbed import load
from ats.log.utils import banner
# Enable logger
logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

# ----------------
# Load the testbed
# ----------------
class CommonSetup(aetest.CommonSetup):
    @aetest.subsection
    def connect(self, testbed):
        """
        establishes connection to all your testbed devices.
        """
        # make sure testbed is provided
        # o assert é uma verificação em tempo de execução de uma condição qualquer
        assert testbed, "Testbed is not provided!"

        # connect to all testbed devices
        #   By default ANY error in the CommonSetup will fail the entire test run
        #   Here we catch common exceptions if a device is unavailable to allow test to continue
        
        try: # O try bloco permite testar um bloco de código quanto a erros.
            testbed.connect()
        
        # O except bloco permite que você lide com o erro.
        except (TimeoutError, StateMachineError, ConnectionError):
            logger.error("Unable to connect to all devices")
        
        # Gerado quando uma função do sistema atingiu o tempo limite no nível do sistema. Corresponde ao erro
        # Uma classe base para problemas relacionados à conexão.
        

class verify_connected(aetest.Testcase):
    """verify_connected
    Garantido uma conexão bem-sucedida com todos os dispositivos no banco de testes.
    """

    @aetest.test
    def test(self, testbed, steps): # Definindo uma função e alocando dados dentro da função
        # Loop over every device in the testbed
        # for se refere no loop, para cada item irá ser executado o bloco de comandos

        # o in serve para traduzir um parâmetro por outro
        for device_name, device in testbed.devices.items():

            # o with serve para facilitar a definição e finalização de um bloco dentro de um código extenso.
            with steps.start(
                f"Test Connection Status of {device_name}", continue_=True
            ) as step:
                # Test "connected" status
                if device.connected:
                    logger.info(f"{device_name} connected status: {device.connected}")
                else:
                    logger.error(f"{device_name} connected status: {device.connected}")
                    step.failed()

# ---------------------------------------
# Execute parser to check interface state
# ---------------------------------------
class TESTCASE_1(aetest.Testcase):
    @aetest.test
    def CHECK(self, SW_ACCESS_1):
        logger.info(banner("Executando parser filtrar parâmetros..."))
        pre_output = SW_ACCESS_1.parse("show interface Ethernet0/2")

        # Verify interface is down before unshutting
        pre_status = pre_output['Ethernet0/2']['oper_status']

        if pre_status == 'down':
            logger.info("\nPASS: Interface Ethernet0/2 está DOWN\n")
        else:
            logger.error("\nFAIL: Interface Ethernet0/2 está UP\n")
            exit()


# -------------------------------------------------
# Unshut the interface by configuring "no shutdown"
# -------------------------------------------------

class TESTCASE_2(aetest.Testcase):
    @aetest.test
    def ATIVANDO(self, SW_ACCESS_1):
        logger.info(banner("Ligando a interface..."))
        SW_ACCESS_1.configure("interface Ethernet0/2\n"
                        " no shutdown")
        logger.info("\nPASS: Interface Ethernet0/2 está UP\n")


# -----
# Sleep
# -----
        logger.info("\n10 segundos para o tráfego na interface entrar em vigor...\n")
        time.sleep(10)


class CommonCleanup(aetest.CommonCleanup):
    """CommonCleanup Section
    < common cleanup docstring >
    """

    # uncomment to add new subsections
    # @aetest.subsection
    # def subsection_cleanup_one(self):
    #     pass


if __name__ == "__main__":
    # for stand-alone execution
    import argparse
    from pyats import topology

    parser = argparse.ArgumentParser(description="standalone parser")
    parser.add_argument(
        "--testbed",
        dest="testbed",
        help="testbed YAML file",
        type=topology.loader.load,
        default=None,
    )

    # do the parsing
    args = parser.parse_known_args()[0]

    aetest.main(testbed=args.testbed)
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