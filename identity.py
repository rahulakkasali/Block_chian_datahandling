# create_identity.py
import uuid

user_name = input("Enter your name: ")
public_key = f"{user_name}_{uuid.uuid4()}"
private_key = f"PRIVATE_{uuid.uuid4()}"

with open("keys.txt", "w") as f:
    f.write(public_key + "\n")
    f.write(private_key)

print("Your public key:", public_key)
