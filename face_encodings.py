import face_recognition_sys

# Load the jpg files into numpy arrays
image = face_recognition_sys.load_image_file("person.jpg")

# Generate the face encodings
face_encodings = face_recognition_sys.face_encodings(image)

if len(face_encodings) == 0:
    # No faces found in the image.
    print("No faces were found.")

else:
    # Grab the first face encoding
    first_face_encoding = face_encodings[0]

    # Print the results
    print(first_face_encoding)
