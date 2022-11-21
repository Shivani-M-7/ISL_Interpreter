import cv2
import mediapipe as mp
from peripherals.lcd_display import *


print("Detection started")
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)
finger_tips = [8, 12, 16, 20]
print("going on!!")
count = 0
while True:
    send_to_lcd(str(count))
    ret, img = cap.read()
    print("1-")
    img = cv2.flip(img, 1)
    print("2-")
    h, w, c = img.shape
    print("3-")
    results = hands.process(img)
    print("4-")
    send_to_lcd(str(count + 16))
    print("5-")
    count += 1
    print(results.multi_hand_landmarks)
    print("6-")
    if results.multi_hand_landmarks:
        for hand_landmark in results.multi_hand_landmarks:
            lm_list = []
            for id, lm in enumerate(hand_landmark.landmark):
                lm_list.append(lm)
            for tip in finger_tips:
                x, y = int(lm_list[tip].x * w), int(lm_list[tip].y * h)
                print(id, ":", x, y)
                cv2.circle(img, (x, y), 15, (255, 0, 0), cv2.FILLED)
            mp_draw.draw_landmarks(img, hand_landmark,
                                    mp_hands.HAND_CONNECTIONS,
                                    mp_draw.DrawingSpec((0, 0, 255), 4, 2)
                                    )
    cv2.imshow("Hand Tracking", img)
    cv2.waitKey(1)
