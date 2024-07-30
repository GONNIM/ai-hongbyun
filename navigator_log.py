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


NAVIGATE_FILE = "navigator_log.csv"


def initialize_csv_file():
    if not os.path.exists(NAVIGATE_FILE):
        with open(NAVIGATE_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['User Key', 'Site Name', 'Site URL', 'Season', 'Timestamp'])


def log_navigator_info(selected_law, law_info):
    initialize_csv_file()

    if st.session_state.user_key and selected_law and law_info:
        season = '1'
        site_url = law_info['link']
        if law_info['link_2']:
            season = '2'
            site_url = law_info['link_2']
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # New Dataframe
        new_data = pd.DataFrame({
            'User Key': [st.session_state.user_key],
            'Site Name': [selected_law],
            'Site URL': [site_url],
            'Season': [season],
            'Timestamp': [timestamp]
        })

        # Save to CSV File
        if os.path.exists(NAVIGATE_FILE):
            existing_data = pd.read_csv(NAVIGATE_FILE)
            combined_data = pd.concat([existing_data, new_data], ignore_index=True)
        else:
            combined_data = new_data

        combined_data.to_csv(NAVIGATE_FILE, index=False)
