from flask import Flask
import time

app = Flask(__name__)

@app.route("/")
def home():
    return "OK - App is running"

@app.route("/timeout-test")
def timeout_test():
    time.sleep(120)  # 2 minutes
    return "Done after 500 seconds"
