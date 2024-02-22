import cv2

cap = cv2.VideoCapture(0)


if not cap.isOpened():
    print("Failed to open webcam")
    exit()


width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('captured_video.avi', fourcc, 20.0, (width, height))


while True:
    
    ret, frame = cap.read()

   
    if not ret:
        print("Failed to read frame")
        break

    
    out.write(frame)

    
    cv2.imshow("Video", frame)

    
    if cv2.waitKey(1) == ord('q'):
        break
