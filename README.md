# 🔍 Domain Scanner & Subdomain Finder (Python)

A simple Python tool for **extracting subdomains, JavaScript files, and links from HTML**, as well as **bruteforcing subdomains** using a wordlist.

This project is intended for **educational purposes, website analysis, and basic security research**.

---

## 🚀 Features

### 🔹 Mode 1 — HTML Analysis
- Extracts subdomains from HTML source code
- Finds `.js` files on the target website
- Collects other links (`href`, `action`)
- Checks HTTP status codes of discovered resources
- Supports absolute and relative URLs

### 🔹 Mode 2 — Subdomain Bruteforce
- Uses a `.txt` wordlist with subdomains
- Combines base URL + subdomain
- Checks which subdomains are alive
- Displays HTTP status codes (`200`, `403`, `404`, etc.)

---

## 📦 Requirements

- Python **3.8+**

Install dependencies:

```bash
pip install requests colorama
