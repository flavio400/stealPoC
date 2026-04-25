# stealPoC
An educative Proof-of-Concept of an infostealer.

# Educational Infostealer Proof of Concept

**For educational and defensive purposes only.**

This repository contains a heavily sanitized and modified version of an infostealer script.  
Its purpose is to help security researchers, blue teamers, and students understand the common techniques used by real-world infostealer malware.

## Important Notice

- This script **does not exfiltrate** any data over the network.
- It **does not** send emails or upload files to any external service.
- All collected data stays on the local machine and is deleted after the demo.
- Screenshots and copied files are for demonstration only.

## What this PoC demonstrates

- Searching for files containing sensitive keywords (wallets, passwords, seeds, etc.)
- Copying browser user data directories (Chrome in this example)
- Generating a device fingerprint using hardware and OS information
- Taking periodic screenshots
- Packaging collected data into a zip archive
- Common persistence and evasion patterns used by infostealers

## Requirements

- Windows operating system
- Python 3.8+
- Administrator privileges are recommended for full functionality

## Installation

```bash
pip install -r requirements.txt
