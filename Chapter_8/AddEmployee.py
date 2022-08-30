import streamlit as st
from typing import Callable
import datetime


class AddEmployee:
    def __init__(self, on_submit: Callable[[str, str, int], bool]):
        st.header("Add a new employee")

        form = st.form("new_employee")
        name = form.text_input("Name")
        dob = str(form.date_input("DOB",
                    min_value=datetime.datetime(year=1920, day=1, month=1)))
        paygrade = form.number_input("paygrade", step=1)

        if form.form_submit_button("Add new Employee"):
            success = on_submit(name, dob, paygrade)
            if success:
                st.success("New employee added")
            else:
                st.error("Employee not added")
