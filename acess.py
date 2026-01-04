# access.py
import json

MY_PUBLIC_KEY = input("Enter your public key: ")
DATA_HASH = input("Enter data hash: ")

with open("blockchain.json") as f:
    chain = json.load(f)

block = next(b for b in chain if b["data_hash"] == DATA_HASH)

if MY_PUBLIC_KEY in block["access"]:
    with open(f"{DATA_HASH}.bin", "rb") as f:
        encrypted = f.read()

    # DEMO DECRYPTION (remove prefix)
    if encrypted.startswith(b"ENCRYPTED::"):
        decrypted = encrypted.replace(b"ENCRYPTED::", b"")

        # SAVE recovered file
        with open("recovered_image.mp4", "wb") as f:
            f.write(decrypted)

        print("ACCESS GRANTED — file saved as recovered_image.mp4")
else:
    print("ACCESS DENIED")
