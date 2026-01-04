import hashlib
import json
import time

# ===== CONFIG =====
FILE_NAME = "/Users/apple/Desktop/BC/_The_Matrix_Resurrections_2021_1080p_Malayalam_multi_audio_.mkv"          # file to upload
OWNER_PUBLIC_KEY = "xx_fd82471a-3a17-4dd2-b5e1-d2da2c9e27fa"
ACCESS_LIST = [
    "vikram_20ec3817-07b6-4256-9400-28f10c8ca718",
    "yy_26550bbe-7d20-4816-9fd6-e1f6243dd35e",
   "vikii_73758dc0-b93a-44b8-a4c6-f2a8f1cc8767",
]
# ==================

# 1. Read file
with open(FILE_NAME, "rb") as f:
    file_data = f.read()

# 2. Encrypt (demo encryption)
encrypted_data = b"ENCRYPTED::" + file_data

# 3. Create hash
data_hash = hashlib.sha256(encrypted_data).hexdigest()

# 4. Store encrypted file (off-chain)
with open(f"{data_hash}.bin", "wb") as f:
    f.write(encrypted_data)

# 5. Load blockchain
with open("blockchain.json", "r") as f:
    blockchain = json.load(f)

# 6. Create new block
new_block = {
    "index": len(blockchain),
    "prev_hash": "HASH",
    "data_hash": data_hash,
    "owner": OWNER_PUBLIC_KEY,
    "access": ACCESS_LIST,
    "time": time.time()
}

# 7. Add block to chain
blockchain.append(new_block)

# 8. Save blockchain
with open("blockchain.json", "w") as f:
    json.dump(blockchain, f, indent=2)

print("UPLOAD SUCCESSFUL ✅")
print("DATA HASH:", data_hash)
