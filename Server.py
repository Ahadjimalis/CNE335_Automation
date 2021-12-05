import os
class Server:
    """ Server class for representing and manipulating servers. """

    def __init__(self, server_ip):
        # TODO -
        self.server_ip = server_ip
        self.ping()

    def ping(self):
        # TODO - Use os module to ping the server
        print("The Server IP is", self.server.ip)
      

        response = os.system("ping -c 1 -w 5 " + self.server_ip + " > /dev/null 2>&1")

        if response == 0:
            return (self.server_ip + "is up and Running")
        else:
            return (self.server_ip + "is Down")


server_ip("3.139.101.224")
print(server.ping())


