import cv2
import numpy as np
from PIL import Image
import os

def create_directory(directory):
    """Create a directory if it does not exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)

def initialize_recognizer_and_detector():
    """Initialize the face recognizer and detector."""
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    if detector.empty():
        print("[ERROR] Haar Cascade file not found.")
        exit()
    return recognizer, detector

def get_images_and_labels(path, detector):
    """Get the images and corresponding labels for training."""
    image_paths = [os.path.join(path, f) for f in os.listdir(path)]
    face_samples = []
    ids = []

    for image_path in image_paths:
        try:
            PIL_img = Image.open(image_path).convert('L')  # Convert to grayscale
            img_numpy = np.array(PIL_img, 'uint8')
            face_id = int(os.path.split(image_path)[-1].split(".")[1])
            faces = detector.detectMultiScale(img_numpy)

            for (x, y, w, h) in faces:
                face_samples.append(img_numpy[y:y+h, x:x+w])
                ids.append(face_id)
        except Exception as e:
            print(f"[ERROR] Skipping file {image_path}: {e}")

    return face_samples, ids

def main():
    dataset_path = 'dataset'
    trainer_dir = 'trainer'
    create_directory(trainer_dir)

    if not os.path.exists(dataset_path):
        print(f"[ERROR] Dataset directory '{dataset_path}' not found.")
        exit()

    recognizer, detector = initialize_recognizer_and_detector()

    print("\n[INFO] Training faces. It will take a few seconds. Wait...")
    faces, ids = get_images_and_labels(dataset_path, detector)

    if len(faces) == 0:
        print("[ERROR] No faces found in the dataset. Exiting.")
        exit()

    recognizer.train(faces, np.array(ids))

    # Save the model into trainer/trainer.yml
    model_path = os.path.join(trainer_dir, 'trainer.yml')
    recognizer.write(model_path)

    print(f"\n[INFO] {len(np.unique(ids))} faces trained. Model saved to '{model_path}'. Exiting Program.")

if __name__ == "__main__":
    main()
