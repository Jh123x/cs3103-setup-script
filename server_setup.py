

import os
import re


CONFIG_TEMPLATE = """\
Host ocna0
    User cs3103
    IdentityFile ~/.ssh/g{group_number}
    Hostname ocna0.d2.comp.nus.edu.sg

Host mini-internet
    User root
    Port 2{padded_group}
    IdentityFile ~/.ssh/g{group_number}
    Hostname mini-internet
    ProxyJump ocna0
"""

SSH_CONFIG_PATH = os.path.expanduser("~/.ssh/config")
DESTINATION_SSH_PATH = os.path.expanduser("~/.ssh/g{group_number}")


if __name__ == '__main__':

    # Get the group number
    group = input('Group number gXX (Just key in XX): ')
    padded_group = group.zfill(3)
    if not group.isdigit():
        print('Group number must be a number.')
        exit(1)

    # Get file to private key
    key_file = input('Private key file: ')
    if not os.path.isfile(key_file):
        print('File does not exist')
        exit(1)


    if(os.path.isfile(SSH_CONFIG_PATH) and input("Do you want to override the current config? (y/n): ") != 'y'):
        exit(0)

    print("Writing to config file")
    with open(SSH_CONFIG_PATH, 'w') as f:
        f.write(CONFIG_TEMPLATE.format(padded_group=padded_group, group_number = (group)))

    print("Copying private key to ~/.ssh with CLRF replaced with LF")
    with open(key_file, 'r') as f:
        key = f.read().replace('\r', '')

    with open(os.path.expanduser(DESTINATION_SSH_PATH.format(group_number=group)), 'w') as f:
        f.write(key)

    print("Setting permissions for private key")
    os.system("chmod 600 ~/.ssh/g{group_number}".format(group_number=group))

    print("Logging into server")
    os.system("ssh mini-internet")
    print("Done")


