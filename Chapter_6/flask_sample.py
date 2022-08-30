from flask import Flask

app = Flask(__name__)


@app.route('/server_status')
def welcome_controller():
    return {
        "message": "Welcome to your Flask Server",
        "status": "up",
        "random": 1 + 1
    }


app.run()
