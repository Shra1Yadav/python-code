# This Python code is used for converting any password/secret to a base64 format
# run this file using this command: python3 <file_name.py>


import base64

# Your Azure Storage Account key as a string
account_key = "IPm8Q~96NXLWa2ckQ7fGxqHd0sqzH97w9_Zm0aSy"

# Convert the key to bytes
key_bytes = account_key.encode('utf-8')

# Encode the bytes to Base64
base64_key = base64.b64encode(key_bytes).decode('utf-8')

print(base64_key)
