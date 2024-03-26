from flask import Flask
app = Flask(__name__)
import datetime

@app.route('/')
def hello_world():
    return f'Thanks for fetching - {datetime.datetime.now()}'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')