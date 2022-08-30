import requests


class API:
    def __init__(self, base_url: str, token: str):
        self.base_url = base_url
        self.base_headers = {"token": token}

    def add_employee(self, name, dob, paygrade):
        try:
            data = {
                "name": name,
                "date_of_birth": dob,
                "paygrade_id": paygrade
            }
            response = requests.post(self.base_url + "/employee",
                                     json=data, headers=self.base_headers)
            if response.status_code == 200:
                return True
        except:
            return False

    def get_employees(self):
        try:
            response = requests.get(self.base_url + "/employees",
                                    headers=self.base_headers)
            return response.json()['data']
        except:
            return None

    def login(self, username, password):
        try:
            response = requests.post(self.base_url + "/auth/login", json={
                "username": username,
                "password": password
            })
            body = response.json()
            token = body.get("token") if type(body) == dict else None

            return token
        except:
            return None

    def is_logged_in(self):
        return requests.get(self.base_url + "/auth/is_logged_in",
                            headers=self.base_headers).status_code == 200
