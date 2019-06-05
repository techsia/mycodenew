#!/user/bin/python3

import os

import paramiko #Best practice: 3rd party import goes after standard

SRVRS = [{'ip':'10.10.2.3', 'un':'bender'}, {'ip':'10.10.2.4', 'un':'fry'}]

with open("cmds2issue.txt", "r") as cmds:
    CMDLIST = cmds.readlines()

def cmdissue(sshsession, commandtoissue): # can use any variable, like x or like commandto issue
    ssh_stdin, ssh_stdout, ssh_stderr = sshsession.exec_command(commandtoissue.rstrip('\n'))
    return ssh_stdout.read().decode('utf-8').rstrip('\n')

def main():
    # harvest RSA key (ssh priv key)
    myprivkey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")

    #loop across servers
    for server in SRVRS:

        # initiate connection to remote machine
        sshsession = paramiko.SSHClient() # Read their documentation for these commands
        sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        sshsession.connect(hostname=server['ip'], username=server['un'], pkey=myprivkey)

        # touch two files

        # get uptime of server
        for commandtoissue in CMDLIST:
            result = cmdissue(sshsession, commandtoissue)
            if result != "":
                with open( (server['ip']).replace(".", "") + ".log", "a" ) as svrlog: # a is for append mode, so you don't write over your script
                    print("COMMAND ISSUED - ", commandtoissue, file=svrlog)
                    print(result, file=svrlog)
                    print("", file=svrlog)
        
        # close the connection
        sshsession.close()

if __name__ == '__main__':
    main()
