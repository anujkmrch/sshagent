'''
Anuj Kumar Chaudhary <me@anujkch.com> anujkch.com

#paramiko ssh client library for python
to install paramiko use the following command

>>> pip install paramiko

if permission is denied for paramiko, use to install
>>> sudo pip install paramiko
'''
import paramiko

'''
# python's internal for os task
'''
import os


def sshCommand(hostname, port, username, password, command):
    try:
        sshclient = paramiko.SSHClient()
        sshclient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        sshclient.load_system_host_keys()
        sshclient.connect(hostname,port,username,password)
        stdin,stdout,stderr = sshclient.exec_command(command)

'''
        # read the output for the ssh client in case you want
        # I recommend to use the distributed application command
        # bash is a wonderful scripting language to maintain the integrity
        # on linux
'''
        # print stdout.read()
        sshclient.close()

    except Exception as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror)
        if e.errno is None:
            print "IAMNULLABLE"

if __name__=="__main__":

    '''
        dictionary of clients list to be initialized
        key represent the ip address or hostname
        value represent the contains the username and password
        user key contains username, pwd key contains password of the current user
    '''

    clients = {
        "192.168.56.101":{"user":"username","pwd":"password"},
        "domain.tld":{"user":"username","pwd":"password"},
        "fqdn.domain.tld":{"user":"username","pwd":"password"}
    }

    for client in clients:
        '''fork the parent process'''
        pid = os.fork()
        if pid == 0:
            # print "I am the child process"
            sshCommand(client,22,clients[client]["user"],clients[client]["pwd"],"touch anujkch.com")
        else:
            # print "I am the parent process"
            os._exit(0)
