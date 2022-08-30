import streamlit as st
from Views import AddEmployee, DisplayEmployees, Login
from API import API
import extra_streamlit_components as stx
import base64, json

cookie_manager = stx.CookieManager()
cookies = cookie_manager.get_all()
authentication_token = cookies.get("token")\
    if type(cookies) == dict else cookies

api = API("http://127.0.0.1:5000/api", authentication_token)


def get_username_from_token(auth_token):
    b64 = str(auth_token).split(".")[1]
    b64 = b64 + "=" * (4 - (len(b64) % 4))
    data = base64.b64decode(b64).decode("utf8")
    username = json.loads(data)['username']
    return username


def manage_login(username, password):
    token = api.login(username, password)
    cookie_manager.set("token", token)
    return token is not None


st.title("Company Management Portal")

if api.is_logged_in():
    st.subheader(f"_Welcome "
                 f"**{get_username_from_token(authentication_token)}**_")
    st.write("_____")
    AddEmployee(api.add_employee)
    st.write("___")
    DisplayEmployees(api.get_employees)
else:
    Login(manage_login)
