import streamlit as st
from typing import Callable


class DisplayEmployees:
    def __init__(self, get_employees: Callable[[], list]):
        st.header("Current Employees")

        employees = get_employees()

        if employees is None:
            st.error("Error getting employees")
        else:
            st.table(employees)
