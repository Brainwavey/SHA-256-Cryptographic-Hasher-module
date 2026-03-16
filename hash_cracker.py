import hashlib
class HashCracker:
    def __init__(self,target_hash, dictionary_file):
        self.hash = target_hash
        self.dict = dictionary_file
    def crack_hash(self):
        try:
            with open ('Passwords.txt','r')as file:
                print(f'[*] FATHOM OS: booting dictionary attack using {self.dict}....\n')
                for line in file:
                    clean_word=line.strip()
                    encoded_word = clean_word.encode('utf-8')
                    hash_object = hashlib.sha256(encoded_word)
                    attempt_hash = hash_object.hexdigest()
                    if attempt_hash == self.hash:
                        print('[!] BREACH SUCCESSFUL [!]')
                        print(f'target hash: {self.hash}')
                        print(f'password: {clean_word}')
                        return
            print('[!] ATTACK FAILED: password not found in the dictionary')
        except FileNotFoundError:
            print(f'[!]ERROR: Could not find"{self.dict}". Make sure it is in your pycharm folder!')
if __name__ == "__main__":
    stolen_hash = "b82f301957da4debf21aaadd01fe54777732d4459dd70a5a751892ec2a4edbdf"
    target_file = "passwords.txt"
    cyber_weapon= HashCracker(stolen_hash, target_file)
    cyber_weapon.crack_hash()