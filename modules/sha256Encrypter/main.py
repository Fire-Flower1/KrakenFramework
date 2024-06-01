import hashlib

result = hashlib.sha256(input("String to hash: ").encode())

print(f"Your hash is {result.hexdigest()}")
