import cv2
import os

# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Create folders for each person
person_folders = ['person1', 'person2']  # Add more folder names as needed
for folder in person_folders:
    os.makedirs(folder, exist_ok=True)

# Set up video capture
cap = cv2.VideoCapture(0)  # Use 0 for webcam, or provide the path to a video file

while True:
    ret, frame = cap.read()  # Read the frame from the video capture

    if not ret:
        break

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Perform face detection
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    # Save detected faces in separate folders
    for (x, y, w, h) in faces:
        face_roi = frame[y:y+h, x:x+w]  # Crop the region of interest containing the face

        # Save the face in the respective person's folder
        folder_name = person_folders[0] if x < frame.shape[1] // 2 else person_folders[1]
        filename = os.path.join(folder_name, f'face_{str(len(os.listdir(folder_name)))}.jpg')
        cv2.imwrite(filename, face_roi)

        # Draw a rectangle around the face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the frame
    cv2.imshow('Face Detection', frame)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
