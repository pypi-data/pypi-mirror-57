import os
import getpass
import socket
from socket import getaddrinfo, AF_INET, gethostname
import subprocess, sys
import json
import requests
import sys
import psutil

class Datanchor():
    def __init__(self):
        self.username = ""
        self.decrypt_url = "http://datanchorlib.prod.datanchor.io/decrypt"
        self.ssid = ""
        self.SSID_LOOKUP = "SSID_LOOKUP"
        self.USER_NAME = "USER_NAME"
        self.platform = sys.platform
    
    def get_username(self):        
        if (self.platform == "win32"):
            self.username = getpass.getuser()
        else:
            self.username = psutil.Process().username()

        return self.username

    def get_host_ip(self): 
        try: 
            host_name = socket.gethostname() 
            return socket.gethostbyname(host_name) 
        except Exception as e: 
            print(type(e))
            print(e)
            print("Unable to get Hostname and IP")
            return None

    def decrypt(self, data):
        print("Decrypting data on " + str(sys.platform) + " platform")
        request_body = {
            "data" : "",
            "context" : "",
            "username" : "",
            "key" : "",
            "myContext" : {}
        }
        request_body["data"] = data["data"]
        request_body["context"] = data["context"]
        request_body["username"] = data["username"]
        request_body["key"] = data["key"]

        my_context = {
            self.USER_NAME : str(self.get_username()),
            self.SSID_LOOKUP : str(self.get_wifi_info())
        }

        request_body["myContext"] = my_context

        headers = { "Content-Type" : "application/json" }

        response = requests.post(self.decrypt_url, json = request_body, headers = headers)

        return response.text
        
    def get_wifi_info(self):
        current_dir = os.path.dirname(__file__)

        if (self.platform == "win32" or self.platform.startswith("win")):
            try:
                if os.path.exists(current_dir + "/wlan_data.json"):
                    os.remove(current_dir + "/wlan_data.json")
            except Exception as e:
                print(type(e))
                print(e)
                print("Wifi information file not found")

            ps1_path = str(current_dir) + "/wifi.ps1"
            output_path = str(current_dir) + "/wlan_data.json"

            try:
                # Netsh WLAN show interfaces
                p = subprocess.Popen(["powershell.exe", ps1_path, ">>", 
                    output_path], 
                    stdout=sys.stdout)
                p.communicate() 

                with open(current_dir + "/wlan_data.json", encoding='utf-16') as json_file:
                    self.ssid = json.load(json_file)["SSID_LOOKUP"]
            except Exception as e:
                print(type(e))
                print(e)
                print("Powershell script failed to execute. Check Set-ExecutionPolicy for your Windows machine.")
                self.ssid = None

        elif (self.platform == "darwin" or self.platform.startswith("darwin")):
            try:
                p1 = subprocess.Popen(['/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport', '-I'], stdout=subprocess.PIPE)
                p2 = subprocess.Popen(['grep', 'SSID'], stdin=p1.stdout, stdout=subprocess.PIPE)
                p3 = subprocess.Popen(['grep', '-v', 'BSSID'], stdin=p2.stdout, stdout=subprocess.PIPE)
                out = p3.communicate()

                self.ssid = out[0].decode('utf-8').lstrip().split()[1].rstrip()
            except Exception as e:
                print(type(e))
                print(e)
                print("Failed to get WiFi info for the MAC platform")
                self.ssid = None

        elif (self.platform.startswith("linux")):
            try:
                p1 = subprocess.Popen(['iwgetid'], stdout=subprocess.PIPE)
                output = p1.communicate() 
                output = output[0].decode('utf-8').split('"')[1]
                self.ssid = output
            except Exception as e:
                print(type(e))
                print(e)
                print("Failed to Wifi info for linux platform by executing iwgetid")
                self.ssid = None
        
        return self.ssid