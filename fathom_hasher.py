import hashlib
class Cryptohasher:
    def __init__(self,raw_password):
        self.raw_data = raw_password
        self.hashed_data = None
    def generate_hash(self):
        encoded_data = self.raw_data.encode("utf-8")
        hash_object = hashlib.sha256(encoded_data)
        self.hashed_data = hash_object.hexdigest()
        print('\n[!] ENCRYPTED SUCCESSFUL')
        print(f'original text: {self.raw_data}')
        print(f'SHA-256 Hash: {self.hashed_data}')
if __name__ == "__main__":
    print('===FATHOM OS CRYPTOGRAPHY MODULE===')
    target_password = input('enter your password or message to encrypt: ')
    security_tool = Cryptohasher(target_password)
    security_tool.generate_hash()