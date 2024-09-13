# ThreatNexus

**ThreatNexus** is an open-source threat intelligence enrichment tool designed to streamline the investigation of suspicious IP addresses, domains, and file hashes. The tool interacts with multiple threat intelligence APIs to provide detailed, actionable data for SOC analysts.

## Features

- **Multiple Input Options**: Analyze IP addresses, domains, and file hashes individually or simultaneously.
- **Threat Intelligence APIs**: Automatically queries sources like VirusTotal, AbuseIPDB, Shodan, and more.
- **Consolidated Report**: Returns a single report with all relevant data about the queried indicators, including reputation scores, geolocation, and threat classifications.

## How it Works

ThreatNexus provides a simple menu interface where the user can select the type of data to investigate:

1. **IP Addresses**: Get details about malicious IPs, including their reputation, geolocation, and any known associations with malicious activity.
2. **Domains**: Query domain names for DNS history, registration details, and associated threats.
3. **File Hashes**: Enrich file hashes (MD5, SHA1, SHA256) to check for known malware signatures and behavior.

The tool can handle one or more inputs simultaneously, making it useful for analyzing complex incidents with multiple threat indicators.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Dqvidd/ThreatNexus.git
   cd threatnexus
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Obtain API keys from the following sources:
   - [VirusTotal](https://developers.virustotal.com/v3.0/reference)
   - [AbuseIPDB](https://docs.abuseipdb.com/)
   - [Shodan](https://developer.shodan.io/)

4. Add your API keys to a `.env` file:
   ```
   VIRUSTOTAL_API_KEY=your_api_key
   ABUSEIPDB_API_KEY=your_api_key
   SHODAN_API_KEY=your_api_key
   
   ...

   ```

## Usage

1. Run the script:
   ```bash
   python threatnexus.py
   ```

2. You will be prompted with a menu where you can select the type of indicator(s) to investigate:
   ```
[*] Welcome to ThreatNexus (Use arrow keys to move, <space> to select, <a> to toggle, <i> to invert)
   ===================================
   ○ IP Address
   ○ Domain Name
   ○ File Hash (MD5/SHA1/SHA256)
   ○ Quit
   ===================================
   ```

3. After selecting, input the data you wish to analyze. ThreatNexus will gather intelligence from various sources and present the findings in a detailed report.

## Example

TODO

```