from imports import *
from utils import *
from auth import *


"""
REST API Call to detect image in a particular picture
Argument takes in image with POST Key as 'file'
Returns JSON of 'face_exists' and 'number_of_faces'
"""
@app.route('/image_detection', methods=['GET', 'POST'])
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
    <title>Have you uploaded a picture yet?</title>
    <h1>Upload a picture and see the number of people in the picture!</h1>
    <form method="POST" enctype="multipart/form-data">
      <input type="file" name="file">
      <input type="submit" value="Upload">
    </form>
    '''


"""
REST APT to render the static page index.html
"""
@app.route('/')
@auth.login_required
def index():
    return render_template('index.html', name='Cycle Project')

"""
Main method to run the Flask Application
"""
if __name__ == '__main__':
    # Set server address 0.0.0.0:5000/
    app.run(host="0.0.0.0", port=5000, debug=True)