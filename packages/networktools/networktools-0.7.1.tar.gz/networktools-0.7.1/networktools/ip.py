import os
import random

"""
To obtain available ports
"""


def network_ip():
    command = "hostname --ip-address"
    retvalue = os.popen(command).readlines()
    return str(retvalue[0][0:-1])
