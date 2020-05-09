"""
network_test_job.py
Example multi-testscript job file
"""
# see https://pubhub.devnetcloud.com/media/pyats/docs/easypy/jobfile.html
# for how job files work

__author__ = "Thiago"
__copyright__ = "Copyright (c) 2019, Cisco Systems Inc."
__contact__ = ["porfiriothiago3@gmail.com"]
__credits__ = []
__version__ = 1.0

import os
from pyats.easypy import run

# Definindo a variável para calcular o caminho local
SCRIPT_PATH = os.path.dirname(__file__)


def main(runtime):
    """job file entrypoint"""

    # run script
    run(
        testscript=os.path.join(SCRIPT_PATH, "pyats-netmiko.py"), # Carregando o script para validar a conexão com os devices
        runtime=runtime,
        taskid="Device Connections",
    )
    '''
    run(
        testscript=os.path.join(SCRIPT_PATH, "interface_errors.py"),
        runtime=runtime,
        taskid="Interface Errors",
    )
'''