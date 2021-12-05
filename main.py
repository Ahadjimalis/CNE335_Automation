# This is the template code for the CNA337 Final Project
# Zachary Rubin, zrubin@rtc.edu
# CNA 337 Fall 2020

import subprocess
import platform

def print_program_info():
    # TODO - Change your name
    print("Server Automator v0.1 by Albert Hadjimalis")

# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    
    # TODO - Create a Server object


def ping(host):
    param = '-n' if platform.system().lower()== 'windows' else '-c'
    command = ['ping', param, '1', host]
    return subprocess.call(command)
    

host = 'ec2-3-139-101-224.us-east-2.compute.amazonaws.com'
print(ping(host))



