from flask import Flask, request
from DataBase import Connection
from DataBase import Employees

app = Flask(__name__)


@app.route('/employees')
def get_all_employees():
    with connection.use_session() as session:
        employees = session.query(Employees).all()
        employees = [employee.to_dict() for employee in employees]
        return {"data": employees}


@app.route('/employee', methods=["POST"])
def add_employee():
    body = request.json
    with connection.use_session() as session:
        session.add(Employees(**body))
        session.commit()
    return {"message": "New employee added successfully"}


connection = Connection("postgresql://postgres:admin@127.0.0.1:5432/CompanyData")
app.run()
