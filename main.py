# This is the template code for the CNA337 Final Project
# Albert Hadjimalis, ahadjima@students.rtc.edu
#Base code provided by Zakary Rubin
# Tutoring from TJ Dewey
#Code from Stack overflow
# CNA 335 Fall 2021



from Server import Server

def print_program_info():
    # TODO - Change your name
    print("Server Automator v0.1 by Albert Hadjimalis")

# This is the entry point to our program


if __name__ == '__main__':
    print_program_info()
    host = Server("ec2-3-139-101-224.us-east-2.compute.amazonaws.com")
    echo = host.ping()
    print(echo)
    host.update()

    
    # TODO - Create a Server object




    






