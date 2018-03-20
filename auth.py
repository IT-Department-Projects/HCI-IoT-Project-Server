from imports import *

# Allowed Extensions of images uploaded to the server
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'JPG'}


# Flask Variables
app = Flask(__name__)
auth = HTTPDigestAuth()


# Secret Key used to protect passwords in Flask
app.config['SECRET_KEY'] = 'Automated Attendance Project'


"""
Users that are allowed to access the Application to upload 
image directly to the server. 
Username and password are stored in a key-value pair format 
for such users.
"""
users = {
    "aiman": "abdullah",
    "salman": "shah",
    "rashika": "chowlek",
    "aniket": "kumar",
    "renu": "chowdhary"
}


"""
Method to check for allowed filenames that are uploaded in the server
Allowed Extensions include 'jpg', 'png', 'jpeg' and 'gif' 
"""
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


"""
Helper method to get password from users
"""
@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None