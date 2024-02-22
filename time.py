import cv2
import time

# Set the video capture device (0 for default camera)
cap = cv2.VideoCapture(0)

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

# Set the duration for video capture in seconds
capture_duration = 2  # Set to the desired duration in seconds

# Get start time
start_time = time.time()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if ret:
        # Display the resulting frame
        cv2.imshow('Frame', frame)

        # Write the frame to the output video file
        out.write(frame)

        # Break the loop if the specified duration has passed
        if time.time() - start_time > capture_duration:
            break

        # Break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything when done
cap.release()
out.release()
cv2.destroyAllWindows()
