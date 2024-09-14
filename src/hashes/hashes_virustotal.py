import re
import threading
import time
import sys
import os
import json
from dotenv import load_dotenv
from virus_total_apis import PublicApi

stop_animation = False
PURPLE_COLOR = "\033[95m"
RESET_COLOR = "\033[0m"
GREEN_COLOR = "\033[92m"

def animation():
    while not stop_animation:
        for i in range(4):
            if stop_animation:
                break
            sys.stdout.write(PURPLE_COLOR + "\rChecking hashes" + "." * i + " " * (3 - i) + RESET_COLOR)
            sys.stdout.flush()
            time.sleep(0.5)

def hashes_virustotal():
    load_dotenv()
    VIRUSTOTAL_API_KEY = os.getenv("VIRUSTOTAL_API_KEY")
    api = PublicApi(VIRUSTOTAL_API_KEY)

    results = {}
    positives = []
    detection = []
    
    animation_thread = threading.Thread(target=animation)
    animation_thread.start()


    # Open and read the file hashes.txt
    with open("hashes.txt", "r") as file:
        hashes = file.readlines()

    # Iterate over each hash
    for hash in hashes:
        hash = hash.strip()  # Remove possible whitespace and line breaks
        response = api.get_file_report(hash)

        if response["results"]["verbose_msg"] == "Scan finished, information embedded":
            positives = response["results"]["positives"]
            detection = []

            for antivirus, data in response["results"]["scans"].items():
                if data["detected"]:
                    detection.append(data["result"])
            
            results[hash] = {
                "positives": positives,
                "detection": detection
            }
        else:
            results[hash] = {
                "positives": 0,
                "detection": ["The hash is not found in the virustotal database."]
            }

        json_results = json.dumps(results, indent=4)
    
    global stop_animation
    stop_animation = True
    animation_thread.join()
    
    print(GREEN_COLOR + "\rHashes has been checked" + RESET_COLOR)
    print()

    return json_results
            
        
    
    
