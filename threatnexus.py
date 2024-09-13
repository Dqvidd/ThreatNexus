from menu import getMenu

__author__ = "Dqvidd"
__version__ = "0.0.1"


choices = getMenu()

def clear_hashes():
    # with open("./results/*", "w") as file:  # Clear the file and leave it empty
        # pass
    pass
    
clear_hashes()

if 'IPs' in choices:
    #Ips()
    print()

if 'Hashes' in choices:
    #Hashes()
    print()

if 'Domains' in choices:
    #Domains()
    print()