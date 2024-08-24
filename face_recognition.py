import cv2
import numpy as np
import os

def load_trained_model(model_path):
    """Load the LBPH face recognizer model."""
    if not os.path.exists(model_path):
        print(f"[ERROR] Model file '{model_path}' not found.")
        exit()
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read(model_path)
    return recognizer

def load_face_cascade(cascade_path):
    """Load the Haar Cascade for face detection."""
    if not os.path.exists(cascade_path):
        print(f"[ERROR] Haar Cascade file '{cascade_path}' not found.")
        exit()
    return cv2.CascadeClassifier(cascade_path)

def load_names(names_path=None):
    """Load names from a file or use default names."""
    if names_path and os.path.exists(names_path):
        with open(names_path, 'r') as file:
            names = [line.strip() for line in file.readlines()]
    else:
        # Default names related to IDs
        names = ['None', 'User1', 'User2']
    return names

def initialize_camera(width=640, height=480):
    """Initialize the video capture device."""
    cam = cv2.VideoCapture(0)
    cam.set(3, width)  # Set video width
    cam.set(4, height) # Set video height
    return cam

def main():
    model_path = 'trainer/trainer.yml'
    cascade_path = 'haarcascade_frontalface_default.xml'
    names_path = None  # Add a path to a file if you want to load names from a file

    recognizer = load_trained_model(model_path)
    face_cascade = load_face_cascade(cascade_path)
    names = load_names(names_path)

    cam = initialize_camera()
    font = cv2.FONT_HERSHEY_SIMPLEX
    min_w = 0.1 * cam.get(3)
    min_h = 0.1 * cam.get(4)

    print("[INFO] Starting real-time face recognition...")

    while True:
        ret, img = cam.read()
        if not ret:
            print("[ERROR] Failed to capture image from camera.")
            break

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(int(min_w), int(min_h)),
        )

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            id, confidence = recognizer.predict(gray[y:y + h, x:x + w])

            # Check if confidence is less than 100 (0 is a perfect match)
            if confidence < 100:
                name = names[id] if id < len(names) else "Unknown"
                confidence_text = "  {0}%".format(round(100 - confidence))
            else:
                name = "Unknown"
                confidence_text = "  {0}%".format(round(100 - confidence))

            cv2.putText(img, name, (x + 5, y - 5), font, 1, (255, 255, 255), 2)
            cv2.putText(img, confidence_text, (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)

        cv2.imshow('camera', img)

        k = cv2.waitKey(10) & 0xff  # Press 'ESC' to exit
        if k == 27:
            break

    print("\n[INFO] Exiting Program and cleaning up...")
    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
