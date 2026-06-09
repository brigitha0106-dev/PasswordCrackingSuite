 🔐 Password Cracking & Credential Attack Suite

## Overview

Password Cracking & Credential Attack Suite is a cybersecurity internship project developed using Python and Streamlit. The project demonstrates password security assessment techniques through ethical simulations and analysis tools. It helps evaluate password strength, identify weak credentials, generate custom dictionaries, analyze password hashes, and estimate resistance against brute-force attacks.

The project is intended for educational and cybersecurity awareness purposes only.

---

## Features

 🔐 Password Auditor

* Password strength analysis
* Entropy calculation
* Dictionary-based password detection
* Risk severity classification
* Security recommendations

 📖 Dictionary Generator

* Generates custom password wordlists
* Supports user-based patterns:

  * Name
  * Birth Year
  * Pet Name
* Includes password variations and mutations

 #️⃣ Hash Generator

* Generates multiple hash formats:

  * MD5
  * SHA1
  * SHA256
  * SHA512
* Demonstrates secure password storage concepts

 🔍 Hash Identifier

* Identifies hash algorithms based on hash length
* Supports:

  * MD5
  * NTLM
  * SHA1
  * SHA256
  * SHA512
* Provides security risk assessment

 ⚡ Brute Force Simulator

* Calculates password keyspace
* Estimates cracking time
* Supports multiple attack speeds:

  * Basic CPU
  * Modern CPU
  * GPU Cluster

 📄 Security Report Generator

* Generates PDF security audit reports
* Includes:

  * Password metrics
  * Entropy values
  * Risk ratings
  * Recommendations

---
## Technology Stack

### Programming Language

* Python

### Libraries Used

* Streamlit
* ReportLab
* Passlib
* Hashlib

### Development Environment

* Kali Linux
* VirtualBox
* GitHub

---

## Project Architecture

```text
User
 │
 ▼
Streamlit Web Interface
 │
 ├── Password Auditor
 ├── Dictionary Generator
 ├── Hash Generator
 ├── Hash Identifier
 ├── Brute Force Simulator
 │
 ▼
Security Analysis Engine
 │
 ▼
PDF Report Generation
```

---

## Project Structure

```text
PasswordCrackingSuite/
│
├── app.py
├── main.py
├── requirements.txt
│
├── modules/
│   ├── password_auditor.py
│   ├── strength_checker.py
│   ├── entropy.py
│   ├── dictionary_generator.py
│   ├── hash_generator.py
│   ├── hash_identifier.py
│   ├── bruteforce_simulator.py
│   ├── report_generator.py
│   └── shadow_parser.py
│
├── sample_data/
├── reports/
└── README.md
```

---

## Deployment

The application is deployed using Streamlit Community Cloud.

### Live Demo

Add your Streamlit deployment URL here:

https://YOUR-STREAMLIT-APP.streamlit.app

---

## Installation

Clone the repository:

```bash
git clone https://github.com/brigitha0106-dev/PasswordCrackingSuite.git
cd PasswordCrackingSuite
```

Create virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run locally:

```bash
streamlit run app.py
```

---

## Expected Outputs

* Password security analysis
* Entropy calculations
* Hash generation results
* Hash identification results
* Brute-force attack simulations
* Security audit PDF reports

---

## Educational Disclaimer

This project is developed strictly for educational, research, and cybersecurity awareness purposes. All password-cracking activities are simulated and performed within controlled environments. The project must not be used against systems without proper authorization.

---
 Author
Hanna Bregitha Thomas

