# create_chain.py
import json, time

genesis = {
    "index": 0,
    "prev_hash": "0",
    "data_hash": "GENESIS",
    "owner": "A",
    "access": [],
    "time": time.time()
}

with open("blockchain.json", "w") as f:
    json.dump([genesis], f, indent=2)

print("Blockchain created")
