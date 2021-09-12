import sys
import paramiko
from paramiko import SSHClient, AutoAddPolicy, AuthenticationException, BadHostKeyException, PasswordRequiredException, SSHException # Connection to a server with SSH protocol using paramiko library
import getpass

class SSH:
# SSH Class

    ssh = paramiko.SSHClient() # Attribute that instantiates the SSHClient class

    def connection(self, server, port, user, password):
        # Method to connect the client in a server

        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # Get private key
        self.ssh.connect(server, port, user, password, timeout = 20) # Connection to server

    def commands(self):
        # Method to execute remote commands

        command = ""
        while command != "exit":
            command = input("> ")
            stdin, stdout, stderr = self.ssh.exec_command(command) # Simple command
            for line in iter(stdout.readline, ''):
                # Return the results of command

                print('\033[32m' + line)

    def close_connection(self):
        # Method to close the connection

        self.ssh.close()

class Menu:
    def initialization(self):
        # Return tuple with data of server

        print('\033[32m' + '******************************************************************************')
        print('\033[32m' + '******************* REMOTE ACCESS MACHINE ************************************')
        print('\033[32m' + '******************************************************************************')
        server = input('\033[32m' + "Enter the server: ")
        port = input('\033[32m' + "Enter the port: ")
        username = input('\033[32m' + "Enter the user: ")
        password = getpass.getpass()
        return server, port, username, password

menu = Menu() # Instantiates the Menu class
server, port, username, password = menu.initialization() # Initialize the menu

ssh = SSH() # Instantiates the SSH Class

try:
    connection = ssh.connection(server, port, username, password) # Send to connection method, the server configurations
except SSHException as e:
    print('\033[32m' + 'Authentication error')
    sys.exit(0)
except BadHostKeyException as bhke:
    print('\033[32m' + 'Your private key is bad')
    sys.exit(0)
except PasswordRequiredException:
    ṕrint('\033[32m' + 'You dont enter with password')
    sys.exit(0)

ssh.commands() # Execute the commands
ssh.close_connection() # Close the connection
print('\033[32m' + 'Connection closed')
