# app.py - a minimal flask api using flask_restful
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Rismi - 165410108"

if __name__ == '__main__':
    port = int(os.environ.get("PORT",8000))
    app.run(debug=True, host='0.0.0.0', port=port)