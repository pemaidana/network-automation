'''
pyATS Library Sample Job File
'''

# Author
__author__ = 'Cisco Systems Inc.'
__copyright__ = 'Copyright (c) 2019, Cisco Systems Inc.'
__contact__ = ['asg-genie-support@cisco.com']
__date__= 'October 2019'

# Python
import os

# pyATS Library
from genie.harness.main import gRun


def main(runtime):

    gRun(trigger_datafile='trigger_datafile.yaml',
         trigger_uids=['TriggerShutNoShutBgp'],
         )