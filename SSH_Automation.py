#Albert Hadjimalis

import Server
import paramiko

def print_program_info():
    # TODO - Change your name
    print("Server Automator v0.1 by Albert Hadjimalis")

# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()

    # TODO - Create a Server object


    server = Server.Server("3.139.101.224")
    print(Server.ping())


    server.ssh_and_update()
