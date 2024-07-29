import streamlit as st # type: ignore
import pandas as pd
import socket
import os
import csv
import platform
import requests
import hashlib
from datetime import datetime
from getmac import get_mac_address # type: ignore


LOG_FILE = "visitor_log.csv"


def initialize_csv_file():
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['User Key', 'Generated Time', 'Device Info', 'Location'])


def log_visitor_info():
    initialize_csv_file()

    system_info = get_system_info()
    user_location = get_location()
    # Generate Unique Key
    unique_key = generate_unique_key(system_info)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ip_address = socket.gethostbyname(socket.gethostname())
    # user_agent = st.get_option('browser.user_agent')

    # New Dataframe
    new_data = pd.DataFrame({
        'User Key': [unique_key],
        'System Info': [system_info],
        'Timestamp': [timestamp],
        'IP Address': [ip_address],
        # 'User-Agent': [user_agent],
        'User Location': [user_location]
    })

    # Save to CSV File
    if os.path.exists(LOG_FILE):
        existing_data = pd.read_csv(LOG_FILE)
        combined_data = pd.concat([existing_data, new_data], ignore_index=True)
    else:
        combined_data = new_data

    combined_data.to_csv(LOG_FILE, index=False)


# Get System Info
def get_system_info():
    # MAC Address
    mac_address = get_mac_address()

    # CPU ID
    cpu_id = ""
    if platform.system() == "Windows":
        cpu_id = os.popen("wmic cpu get processorid").read().strip().split('\n')[1]
    elif platform.system() == "Linux":
        cpu_id = os.popen("cat /proc/cpuinfo | grep Serial | cut -d ' ' -f 2").read().strip()
    elif platform.system() == "Darwin":
        cpu_id = os.popen("sysctl -n machdep.cpu.brand_string").read().strip()

    system_info = f"{mac_address}-{cpu_id}"
    return system_info


# Get Location
def get_location():
    try:
        response = requests.get('https://ipinfo.io')
        data = response.json()
        return data['city'] + ', ' + data['country']
    except:
        return "Unknown"


# Generate Unique Key
def generate_unique_key(system_info):
    unique_key = hashlib.sha256(system_info.encode()).hexdigest()
    return unique_key
