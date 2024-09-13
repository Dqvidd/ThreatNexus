import re
import threading
import time
import sys
import os
from dotenv import load_dotenv

VIRUSTOTAL_API_KEY = os.gotenv('VIRUSTOTAL_API_KEY')

stop_animation = False
PURPLE_COLOR = "\033[95m"
RESET_COLOR = "\033[0m"
GREEN_COLOR = "\033[92m"

# def animation():
#     while not stop_animation:
#         for i in range(4):
#             if stop_animation:
#                 break
#             sys.stdout.write(PURPLE_COLOR + "\rChecking hashes" + "." * i + " " * (3 - i) + RESET_COLOR)
#             sys.stdout.flush()
#             time.sleep(0.5)

def hashes():
    # animation_thread = threading.Thread(target=animation)
    # animation_thread.start()

    # Clear the files before starting
    
    
    # Open and read the file hashes.txt
    with open('hashes.txt', 'r') as file:
        hashes = file.readlines()

    # Iterate over each hash
    for hash in hashes:
        hash = hash.strip()  # Remove possible whitespace and line breaks
        response = VIRUSTOTAL_API_KEY.get_file_report(hash)

    
    print(response)
            
        
    
    # global stop_animation
    # stop_animation = True
    # animation_thread.join()
    
    print(GREEN_COLOR + "\rResults have been saved in ./results/..." + RESET_COLOR)
    print()
