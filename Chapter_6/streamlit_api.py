import streamlit as st
import requests
import datetime

url = "http://127.0.0.1:5000"


def add_employee(name, dob, paygrade):
    data = {
        "name": name,
        "date_of_birth": dob,
        "paygrade_id": paygrade
    }
    response = requests.post(url + "/employee", json=data)
    if response.status_code == 200:
        return True
    return False


def get_employees():
    response = requests.get(url + "/employees")
    return response.json()['data']


form = st.form("new_employee")
name = form.text_input("Name")
dob = str(form.date_input("DOB", min_value=datetime.datetime(year=1920, day=1, month=1)))
paygrade = form.number_input("paygrade", step=1)

if form.form_submit_button("Add new Employee"):
    if add_employee(name, dob, paygrade):
        st.success("Employee Added")
    else:
        st.error("Error adding employee")

st.write("___")

employees = get_employees()
st.table(employees)
