import cv2
import os

def identify_frame(frame):
    # Your identification criteria here
    # Example: check if the frame contains a certain object or pattern
    return True  # Return True if identified, else False

def crop_frame(frame, x, y, width, height):
    cropped_frame = frame[y:y+height, x:x+width]
    return cropped_frame

def process_video(input_path, output_folder):
    # Open the video file
    video_capture = cv2.VideoCapture(input_path)

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Read the first frame
    success, frame = video_capture.read()
    frame_number = 0

    while success:
        if identify_frame(frame):
            cropped_frame = crop_frame(frame, x, y, width, height)

            # Save the cropped frame to the output folder
            output_path = os.path.join(output_folder, f"cropped_frame_{frame_number}.png")
            cv2.imwrite(output_path, cropped_frame)
            frame_number += 1

        success, frame = video_capture.read()

    # Release resources
    video_capture.release()
    cv2.destroyAllWindows()

# Specify your input video file and output folder
input_video_path = "C:\\Users\\DevAppSys Office\\Downloads\\WhatsApp Video 2024-01-29 at 11.18.49 AM.mp4"
output_frames_folder = "F:\rr"

# Specify the crop region (x, y, width, height)
x, y, width, height = 100, 100, 200, 200

# Process the video and save cropped frames to the output folder
process_video(input_video_path, output_frames_folder)
