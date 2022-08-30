from jwt import PyJWT
from time import time
from typing import Union


class JWTService:
    expires_in_seconds = 2592000
    signing_algorithm = "HS256"

    def __init__(self, signing_key: str, expires_in_seconds: int = 2592000):
        self.signing_key = signing_key
        self.expires_in_seconds = expires_in_seconds

    def generate(self, data: dict, expires_in_seconds: int = expires_in_seconds) -> Union[str, None]:
        try:
            instance = PyJWT()

            curr_unix_epoch = int(time())
            data['iat'] = curr_unix_epoch

            if isinstance(expires_in_seconds, int):
                data['exp'] = curr_unix_epoch + expires_in_seconds

            token = instance.encode(payload=data, key=self.signing_key, algorithm=self.signing_algorithm)

            if type(token) == bytes:
                token = token.decode('utf8')  # Needed for some versions of PyJWT

            return token
        except BaseException as _:
            return None

    def is_valid(self, token: str, verify_time: bool = True) -> bool:
        try:
            payload = self.get_payload(token)

            if payload is None:
                return False

            if verify_time and 'exp' in payload and payload['exp'] < int(time()):
                return False

            return True
        except:
            return False

    def get_payload(self, token: str):
        try:
            instance = PyJWT()
            payload = instance.decode(jwt=token, key=self.signing_key, algorithms=[self.signing_algorithm])
            return payload
        except Exception as e:
            print(e)
            return None
