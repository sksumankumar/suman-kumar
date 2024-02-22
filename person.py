import cv2
import os

# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Create directories to save the captured faces
save_directory_1 = 'faces_1'
save_directory_2 = 'faces_2'
if not os.path.exists(save_directory_1):
    os.makedirs(save_directory_1)
if not os.path.exists(save_directory_2):
    os.makedirs(save_directory_2)

# Initialize the video capture
video_capture = cv2.VideoCapture(0)

while True:
    # Read a frame from the video capture
    ret, frame = video_capture.read()
    
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Perform face detection
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # Draw rectangles around the detected faces and save them
    for i, (x, y, w, h) in enumerate(faces):
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Save the face image in the respective save_directory
        if i == 0:
            save_path = os.path.join(save_directory_1, f'face_{len(os.listdir(save_directory_1))}.jpg')
        else:
            save_path = os.path.join(save_directory_2, f'face_{len(os.listdir(save_directory_2))}.jpg')
        
        face_image = frame[y:y+h, x:x+w]
        cv2.imwrite(save_path, face_image)

    # Display the resulting frame
    cv2.imshow('Video', frame)
    
    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close the window
video_capture.release()
cv2.destroyAllWindows()
