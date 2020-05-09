"""
testbed_connection.py
Verify that all devices in the testbed can be successfully connected to.
"""
# see https://pubhub.devnetcloud.com/media/pyats/docs/aetest/index.html
# for documentation on pyATS test scripts

__author__ = "Thiago"
__copyright__ = "Copyright (c) 2019, Cisco Systems Inc."
__contact__ = ["porfiriothiago3@gmail.com"]
__credits__ = []
__version__ = 1.0

import re
import logging
from pyats import aetest
from unicon.core.errors import TimeoutError, StateMachineError, ConnectionError

# create a logger for this module
logger = logging.getLogger(__name__)


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

            # o with serve para facilitar a definição e finalizaçaõ de um bloco dentro de um código extenso.
            with steps.start(
                f"Test Connection Status of {device_name}", continue_=True
            ) as step:
                # Test "connected" status
                if device.connected:
                    logger.info(f"{device_name} connected status: {device.connected}")
                else:
                    logger.error(f"{device_name} connected status: {device.connected}")
                    step.failed()

@aetest.loop(device = ('SW_CORE_1'))
class PingTestcase(aetest.Testcase):

    @aetest.test.loop(destination = ('192.168.36.210'))
    def ping(self, device, destination):
        try:
            result = self.parameters[device].ping(destination)

        except Exception as e:
            self.failed('Ping {} from device {} failed with error: {}'.format(
                                destination,
                                device,
                                str(e),
                            ),
                        goto = ['exit'])
        else:
            match = re.search(r'Success rate is (?P<rate>\d+) percent', result)
            success_rate = match.group('rate')

            logger.info('Ping {} with success rate of {}%'.format(
                                        destination,
                                        success_rate,
                                    )
                               )

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