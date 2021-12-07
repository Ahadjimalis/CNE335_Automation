import os
import subprocess
import platform
import paramiko

class Server:
    """ Server class for representing and manipulating servers. """

    def __init__(self, server_ip):
        # TODO -
        self.ip = server_ip


    # def ping(self):
    #     # TODO - Use os module to ping the server
    #
    #
    #     response = os.system("ping -n 1 -w 5 " + self.ip + " > /dev/null 2>&1")
    #
    #     if response == 0:
    #         return (self.ip + "is up and Running")
    #     else:
    #         return (self.ip + "is Down")

    def ping(self):
        param = '-n' if platform.system().lower()== 'windows' else '-c'
        command = ['ping', param, '1', self.ip]
        return subprocess.call(command)

    def update(self):
        address = self.ip
        remote = paramiko.SSHClient()
        remote.load_system_host_keys()
        remote.connect(hostname=self.ip, username="ubuntu", password="")
        if remote.get_transport() is not None:
            activity = remote.get_transport().is_active()
            print("transport active", activity)
        command = "sudo apt-get update -y"
        first, out, err = remote.exec_command(command)
        first.flush()
        data = out.read().splitlines()
        for line in data:
            print(line)

        command = "sudo apt-get upgrade -y"
        first, out, err = remote.exec_command(command)
        first.flush()
        data = out.read().splitlines()
        for line in data:
            print(line)
        remote.close()




# server = server("3.139.101.224")
# print(server.ping())


