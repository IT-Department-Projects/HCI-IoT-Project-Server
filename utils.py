from imports import *
"""
Method to detect faces in an image.
Returns two values in the form of JSON:
1. Whether any face exisits in the image
2. The number of faces that exist in the image
"""


def detect_faces_in_image(file_stream):

    # Load the uploaded image file
    img = face_recognition.load_image_file(file_stream)
    # Get face encodings for any faces in the uploaded image
    unknown_face_encodings = face_recognition.face_encodings(img)

    face_found = False
    number_of_faces = 0
    '''
        To Do: 
        Return List of names of files whose images 
        are there in the given picture
    '''

    if len(unknown_face_encodings) > 0:
        face_found = True
        number_of_faces = len(unknown_face_encodings)

    # Return the result of names of people as json
    result = {
        "face_exists": face_found,
        "number_of_faces": number_of_faces

    }
    return jsonify(result)
