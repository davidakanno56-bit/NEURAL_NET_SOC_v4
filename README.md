# NEURAL_NET_SOC_v4
Automated SOC monitoring tool and telemetry analysis pipeline designed for real-time auth log parsing, brute-force threat detection, and SIEM integration. Built for Akanno Labs.
# NEURAL_NET SOC v4.0

An automated threat monitoring and log analysis engine designed to process host authentication logs, detect brute-force activity, and supply structured security telemetry to enterprise cloud SIEM platforms.

## ⚡ Core Features
* **Authentication Log Parsing:** Automated regex extraction of target IPs and failed login parameters from `/var/log/auth.log`.
* **Threshold Alerting:** Dynamic threat scoring to isolate potential brute-force attacks in real time.
* **SQL Telemetry Queries:** Custom relational queries for historical log correlation and incident response.
* **SIEM Compatibility:** Structured output ready for Elastic Agent ingestion and cloud dashboard visualization.

## 🚀 Tech Stack
* **Language:** Python 3.x
* **Database Querying:** PostgreSQL / Standard SQL
* **Environment:** Ubuntu Linux (VirtualBox) / Elastic Cloud SIEM
