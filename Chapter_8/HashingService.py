import bcrypt


class HashingService:
    def __init__(self, bcrypt_gen_salt: int = 12):
        self.gen_salt = bcrypt_gen_salt

    def hash_bcrypt(self, plain_text: bytes) -> bytes:
        return bcrypt.hashpw(plain_text, bcrypt.gensalt(self.gen_salt))

    def check_bcrypt(self, plain_text: bytes, hashed_password: bytes) -> bool:
        try:
            return bcrypt.checkpw(plain_text, hashed_password)
        except:
            return False
