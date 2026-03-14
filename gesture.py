# gestures.py
# Finger landmark mapping using MediaPipe
# 21 landmarks per hand — 0 = wrist, 4,8,12,16,20 = fingertips

def get_finger_states(landmarks):
    """
    Returns list of 5 booleans — True if finger is UP
    Order: [Thumb, Index, Middle, Ring, Pinky]
    """
    fingers = []

    # Thumb — compare tip (4) with IP joint (3) on x-axis
    if landmarks[4].x < landmarks[3].x:
        fingers.append(True)   # Thumb UP
    else:
        fingers.append(False)  # Thumb DOWN

    # Other 4 fingers — compare tip with PIP joint on y-axis
    # Lower y value = higher on screen = finger is UP
    tips = [8, 12, 16, 20]
    pip  = [6, 10, 14, 18]

    for tip, p in zip(tips, pip):
        if landmarks[tip].y < landmarks[p].y:
            fingers.append(True)   # Finger UP
        else:
            fingers.append(False)  # Finger DOWN

    return fingers


def detect_gesture(fingers):
    """
    Maps finger states to gesture/letter name.
    fingers = [Thumb, Index, Middle, Ring, Pinky]
    """
    thumb, index, middle, ring, pinky = fingers

    # --- Letters ---
    if fingers == [False, True, False, False, False]:
        return "D / Pointing"

    if fingers == [False, True, True, False, False]:
        return "V / Peace / Victory"

    if fingers == [False, True, True, True, False]:
        return "W / Three Fingers"

    if fingers == [False, True, True, True, True]:
        return "B / Four Fingers"

    if fingers == [True, True, True, True, True]:
        return "5 / Open Hand"

    if fingers == [False, False, False, False, False]:
        return "Fist / A / S / E"

    if fingers == [True, False, False, False, False]:
        return "Thumb Up / A"

    if fingers == [False, False, False, False, True]:
        return "Pinky / I"

    if fingers == [True, True, False, False, True]:
        return "Y / ILY (I Love You)"

    if fingers == [True, False, False, False, True]:
        return "Y / Hang Loose"

    if fingers == [False, True, False, False, True]:
        return "Rock On / Horns"

    if fingers == [True, True, True, False, False]:
        return "Three / W"

    if fingers == [True, False, True, True, True]:
        return "Four (Thumb in)"

    if fingers == [True, True, False, False, False]:
        return "Gun / L Shape"

    if fingers == [False, False, True, False, False]:
        return "Middle Finger"

    return "Unknown Gesture"