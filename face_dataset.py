import cv2
import os

def create_directory(directory):
    """Create the directory if it does not exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)

def initialize_camera():
    """Initialize the camera and set video parameters."""
    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        print("[ERROR] Could not access the camera.")
        exit()
    cam.set(3, 480)  # set video width
    cam.set(4, 640)  # set video height
    return cam

def main():
    dataset_dir = 'dataset'
    create_directory(dataset_dir)

    # Load Haar Cascade for face detection
    face_cascade_path = 'haarcascade_frontalface_default.xml'
    if not os.path.isfile(face_cascade_path):
        print("[ERROR] Haar Cascade file not found.")
        exit()

    face_detector = cv2.CascadeClassifier(face_cascade_path)
    cam = initialize_camera()

    face_id = input('\nEnter user ID and press <return> ==> ')

    print("\n[INFO] Initializing face capture. Look at the camera and wait...")
    count = 0

    while True:
        ret, img = cam.read()
        if not ret:
            print("[ERROR] Failed to grab frame.")
            break

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            count += 1

            # Save the captured image into the dataset directory
            face_image = gray[y:y+h, x:x+w]
            cv2.imwrite(f"{dataset_dir}/User.{face_id}.{count}.jpg", face_image)

            cv2.imshow('image', img)

        k = cv2.waitKey(100) & 0xff  # Press 'ESC' to exit
        if k == 27:
            break
        elif count >= 30:  # Take 30 face samples and stop video
            break

    # Clean up
    print("\n[INFO] Exiting Program and cleanup.")
    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
