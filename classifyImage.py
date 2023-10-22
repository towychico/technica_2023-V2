import cv2
import mediapipe as mp
import pickle
import numpy as np

def classify_hand_gesture(image_path):
    model_dict = pickle.load(open('./model.p', 'rb'))
    model = model_dict['model']

    mp_hands = mp.solutions.hands
    mp_drawing = mp.solutions.drawing_utils

    # Model Confidence
    hands = mp_hands.Hands(static_image_mode=True, min_tracking_confidence=0.3)

    # Load the image
    frame = cv2.imread(image_path)

    data_aux = []

    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            for i in range(len(hand_landmarks.landmark)):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y
                data_aux.append(x)
                data_aux.append(y)
        prediction = model.predict([np.asarray(data_aux)])
        letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q', 'R', 'S','T', 'U','V','W','X',
                   'Y','Z' ]
        return letters(prediction[0])

    return None  # Return None if no hand landmarks were found

# Example usage:
image_path = 'Test.jpeg'  # Replace with the actual image path
result = classify_hand_gesture(image_path)
if result is not None:
    print(f"Hand gesture classification: {result}")
else:
    print("No hand landmarks found in the image.")


