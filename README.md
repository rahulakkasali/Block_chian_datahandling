# 🔗 Decentralized Data Sharing using Blockchain Principles

![Blockchain](https://img.shields.io/badge/Blockchain-Decentralized-blue)
![Python](https://img.shields.io/badge/Python-3.x-yellow)
![Security](https://img.shields.io/badge/Security-Cryptography-green)
![Status](https://img.shields.io/badge/Status-Demo%20Project-orange)

---

## 📌 Project Overview

This project demonstrates a **blockchain-inspired, decentralized data sharing system** where users can securely share files (photos, videos, documents) **without using a central server or database**.

Instead of storing data on the blockchain, the system:
- Stores **encrypted files off-chain**
- Uses a **blockchain ledger only for permissions, ownership, and integrity**
- Allows **only authorized users** to access shared data

👉 This project focuses on **blockchain as a technology**, not cryptocurrency or payments.

---

## 🧠 Core Idea

> **Blockchain controls trust and permissions.  
Encrypted storage holds the actual data.  
Keys decide access.**

---

## ✨ Key Features

🔐 Decentralized Identity (Public/Private Keys)  
📜 Blockchain-style immutable ledger (`blockchain.json`)  
📦 Off-chain encrypted file storage  
✅ Permission-based access control  
🚫 No central server  
🚫 No central database  
🧪 Fully runnable demo using Python  



---

## 🔁 Workflow (End-to-End)

1️⃣ User creates a decentralized identity  
2️⃣ Blockchain (ledger) is initialized  
3️⃣ User uploads a file:
   - File is encrypted locally
   - Encrypted file stored off-chain
   - Blockchain records:
     - File hash
     - Owner
     - Access permissions
4️⃣ Other users attempt access:
   - Blockchain checks permission
   - Allowed users decrypt and view file
   - Unauthorized users are denied

---

## 🧪 Demo Scenario

Example users: **A, B, C, D**

- **B uploads a video**
- **B allows access only to C**
- Results:

| User | Access |
|----|----|
| B | ✅ Allowed |
| C | ✅ Allowed |
| A | ❌ Denied |
| D | ❌ Denied |

Even though all users have the encrypted file, **only permitted users can view it**.

---

## 🗂️ Project Structure







---

## 🧱 System Architecture


