import json
from flask import Flask, request, Response, render_template, abort, url_for, jsonify, redirect
from flask_httpauth import HTTPDigestAuth
from flask_migrate import Migrate
import gevent
import time
from flask_httpauth import HTTPDigestAuth

import face_recognition

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

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


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/image_recognition', methods=['GET', 'POST'])
def upload_image():
    # Check if a valid image file was uploaded
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            return redirect(request.url)

        if file and allowed_file(file.filename):
            # The image file seems valid! Detect faces and return the result.
            return detect_faces_in_image(file)

    # If no valid image file was uploaded, show the file upload form:
    return '''
    <!doctype html>
    <title>Is this a picture of Obama?</title>
    <h1>Upload a picture and see if it's a picture of Obama!</h1>
    <form method="POST" enctype="multipart/form-data">
      <input type="file" name="file">
      <input type="submit" value="Upload">
    </form>
    '''

'''
Searches for image amongst current encoding values
'''
def detect_faces_in_image(file_stream):

    # Load the uploaded image file
    img = face_recognition.load_image_file(file_stream)
    # Get face encodings for any faces in the uploaded image
    unknown_face_encodings = face_recognition.face_encodings(img)

    '''
        To Do: 
        Return List of names of files whose images 
        are there in the given picture
    '''

    # Return the result of names of people as json
    result = {
        "": ""
    }
    return jsonify(result)


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