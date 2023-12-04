import cv2
import face_recognition

# Get a reference to your webcam (0 is usually the default camera)
cam_pardéfaut = cv2.VideoCapture(0)

known_image = face_recognition.load_image_file('./me.png')
known_face_encoding = face_recognition.face_encodings(known_image)[0]

# Create arrays of known face encodings and corresponding labels
known_face_encodings = [known_face_encoding]
known_face_labels = ['Known Person']

while True:
    # Capture each frame from the webcam
    ret, frame = cam_pardéfaut.read()

    # Find all face locations in the current frame
    face_locations = face_recognition.face_locations(frame)
    # Get face encodings for each face in the current frame
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    # Loop through each face found in the frame
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Check if the face matches the known person
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        name = "Unknown Person"

        # If a match is found, use the label of the known person
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_labels[first_match_index]

        # Draw a rectangle around the face and display the name
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    # Break the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
cam_pardéfaut.release()
cv2.destroyAllWindows()
