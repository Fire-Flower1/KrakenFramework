import hashlib

result = hashlib.md5(input("String to hash: ").encode())

print(f"Your hash is {result.hexdigest()}")
