from src.menu import getMenu
from src.hashes.hashes_virustotal import hashes_virustotal
__author__ = "Dqvidd"
__version__ = "0.0.1"


choices = getMenu()

def clear_hashes():
    # with open("./results/*", "w") as file:  # Clear the file and leave it empty
        # pass
    pass
    
clear_hashes()

if 'IP Address' in choices:
    #Ips()
    print()

if 'Domain Name' in choices:
    #Domains()
    print()

if 'File Hash (MD5/SHA1/SHA256)' in choices:
    hashes_virustotal()
    print()

if 'Quit':
    exit(1)
