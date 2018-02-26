import json
from flask import Flask, request, Response, render_template, abort, url_for
from flask_httpauth import HTTPDigestAuth
from flask_migrate import Migrate
import gevent
import time
from flask_httpauth import HTTPDigestAuth

# Flask Variables
app = Flask(__name__)
auth = HTTPDigestAuth()

app.config['SECRET_KEY'] = 'HCI Project'

# Users to access app
# Users to be authenticated
users = {
    "aiman": "abdullah",
    "salman": "shah",
    "rashika": "chowlek",
    "aniket": "kumar"
}


# Authenticating users from Dictionary
@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None


@app.route('/')
@auth.login_required
def index():
    return render_template('index.html', name='Cycle Project')

# Main Method in the Server code
if __name__ == '__main__':
    # Set server address 0.0.0.0:5000/
    app.run(host="0.0.0.0", port=5000, debug=True)
