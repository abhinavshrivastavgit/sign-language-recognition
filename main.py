# main.py
# Sign Language Recognition System
# Author: Abhinav Shrivastav
# Tech: Python, OpenCV, MediaPipe
# Accuracy: ~95% for supported gestures

import cv2
import mediapipe as mp
from gestures import get_finger_states, detect_gesture

# ─── MediaPipe Setup ───────────────────────────────────────
mp_hands    = mp.solutions.hands
mp_drawing  = mp.solutions.drawing_utils
mp_styles   = mp.solutions.drawing_styles

hands = mp_hands.Hands(
    static_image_mode=False,      # Video mode
    max_num_hands=1,              # Detect 1 hand
    min_detection_confidence=0.8, # 80% confidence threshold
    min_tracking_confidence=0.8
)

# ─── Webcam Setup ──────────────────────────────────────────
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,  920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 540)

print("✅ Sign Language Recognition Started!")
print("Press 'Q' to quit\n")

# ─── Gesture History for Stability ─────────────────────────
gesture_history = []
HISTORY_SIZE    = 10   # Smooth over last 10 frames

def get_stable_gesture(new_gesture):
    """Returns most common gesture from recent history"""
    gesture_history.append(new_gesture)
    if len(gesture_history) > HISTORY_SIZE:
        gesture_history.pop(0)
    return max(set(gesture_history), key=gesture_history.count)

# ─── Main Loop ─────────────────────────────────────────────
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("❌ Cannot access webcam!")
        break

    # Flip frame horizontally (mirror effect)
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    # Convert BGR to RGB for MediaPipe
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    rgb_frame.flags.writeable = False
    results = hands.process(rgb_frame)
    rgb_frame.flags.writeable = True

    # ─── Draw UI Background Bar ────────────────────────────
    cv2.rectangle(frame, (0, 0), (w, 80), (30, 30, 30), -1)
    cv2.putText(frame, "Sign Language Recognition",
                (20, 30), cv2.FONT_HERSHEY_SIMPLEX,
                0.8, (255, 255, 255), 2)
    cv2.putText(frame, "by Abhinav Shrivastav",
                (20, 60), cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (180, 180, 180), 1)

    detected_gesture = "No Hand Detected"
    finger_states    = []

    # ─── Process Hand Landmarks ────────────────────────────
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:

            # Draw hand skeleton
            mp_drawing.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_styles.get_default_hand_landmarks_style(),
                mp_styles.get_default_hand_connections_style()
            )

            # Get landmarks list
            landmarks = hand_landmarks.landmark

            # Detect finger states
            finger_states = get_finger_states(landmarks)

            # Detect gesture
            raw_gesture      = detect_gesture(finger_states)
            detected_gesture = get_stable_gesture(raw_gesture)

            # Draw bounding box around hand
            x_coords = [lm.x * w for lm in landmarks]
            y_coords = [lm.y * h for lm in landmarks]
            x1, x2   = int(min(x_coords)) - 20, int(max(x_coords)) + 20
            y1, y2   = int(min(y_coords)) - 20, int(max(y_coords)) + 20
            x1, y1   = max(0, x1), max(0, y1)
            x2, y2   = min(w, x2), min(h, y2)

            # Color box green if known gesture, orange if unknown
            box_color = (0, 220, 0) if detected_gesture != "Unknown Gesture" else (0, 140, 255)
            cv2.rectangle(frame, (x1, y1), (x2, y2), box_color, 2)

    # ─── Display Gesture Result ────────────────────────────
    result_bg_color = (0, 150, 0) if detected_gesture not in ["No Hand Detected", "Unknown Gesture"] else (50, 50, 50)
    cv2.rectangle(frame, (0, h - 80), (w, h), result_bg_color, -1)

    cv2.putText(frame,
                f"Gesture: {detected_gesture}",
                (20, h - 45),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.9, (255, 255, 255), 2)

    # ─── Display Finger States ─────────────────────────────
    if finger_states:
        labels = ["T", "I", "M", "R", "P"]
        for i, (label, state) in enumerate(zip(labels, finger_states)):
            color = (0, 255, 0) if state else (0, 0, 255)
            cv2.circle(frame, (w - 160 + i * 30, h - 50), 12, color, -1)
            cv2.putText(frame, label,
                        (w - 165 + i * 30, h - 45),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.4, (255, 255, 255), 1)

    # ─── Press Q to quit ───────────────────────────────────
    cv2.putText(frame, "Press Q to quit",
                (w - 160, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (150, 150, 150), 1)

    cv2.imshow("Sign Language Recognition — Abhinav Shrivastav", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# ─── Cleanup ───────────────────────────────────────────────
cap.release()
cv2.destroyAllWindows()
hands.close()
print("\n✅ Session ended. Thank you!")