import cv2
import mediapipe as mp
from peripherals.lcd_display import *

def detect_loop():
    print("Hery!!")
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands()
    mp_draw = mp.solutions.drawing_utils
    cap = cv2.VideoCapture(0)
    finger_tips = [8, 12, 16, 20]
    thumb_tip = 4
    print("starting")
    mode = "Sign"
    while True:
        ret, img = cap.read()
        img = cv2.flip(img, 1)
        h, w, c = img.shape
        results = hands.process(img)
        send_to_lcd("IDKK", "Debug")
        if results.multi_hand_landmarks:
            for hand_landmark in results.multi_hand_landmarks:
                lm_list = []
                for id, lm in enumerate(hand_landmark.landmark):
                    lm_list.append(lm)
                finger_fold_status = []
                for tip in finger_tips:
                    x, y = int(lm_list[tip].x * w), int(lm_list[tip].y * h)
                    # print(id, ":", x, y)
                    # cv2.circle(img, (x, y), 15, (255, 0, 0), cv2.FILLED)

                    if lm_list[tip].x < lm_list[tip - 2].x:
                        # cv2.circle(img, (x, y), 15, (0, 255, 0), cv2.FILLED)
                        finger_fold_status.append(True)
                    else:
                        finger_fold_status.append(False)

                print(finger_fold_status)

                x, y = int(lm_list[8].x * w), int(lm_list[8].y * h)
                print(x, y)

                action = ""
                # stop
                if lm_list[4].y < lm_list[2].y and lm_list[8].y < lm_list[6].y and lm_list[12].y < lm_list[10].y and \
                        lm_list[16].y < lm_list[14].y and lm_list[20].y < lm_list[18].y and lm_list[17].x < lm_list[
                    0].x < \
                        lm_list[5].x:
                    cv2.putText(img, "STOP", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                    send_to_lcd("Stop", mode)
                    

                # Forward
                if lm_list[3].x > lm_list[4].x and lm_list[8].y < lm_list[6].y and lm_list[12].y > lm_list[10].y and \
                        lm_list[16].y > lm_list[14].y and lm_list[20].y > lm_list[18].y:
                    cv2.putText(img, "FORWARD", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                    send_to_lcd("Forward", mode)

                # Backward
                if lm_list[3].x > lm_list[4].x and lm_list[3].y < lm_list[4].y and lm_list[8].y > lm_list[6].y and \
                        lm_list[
                            12].y < lm_list[10].y and \
                        lm_list[16].y < lm_list[14].y and lm_list[20].y < lm_list[18].y:
                    cv2.putText(img, "BACKWARD", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                    print("BACKWARD")
                    send_to_lcd("BACKWARD", mode)

                # Left
                if lm_list[4].y < lm_list[2].y and lm_list[8].x < lm_list[6].x and lm_list[12].x > lm_list[10].x and \
                        lm_list[16].x > lm_list[14].x and lm_list[20].x > lm_list[18].x and lm_list[5].x < lm_list[0].x:
                    cv2.putText(img, "LEFT", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                    print("LEFT")
                    send_to_lcd("LEFT", mode)

                # Right
                if lm_list[4].y < lm_list[2].y and lm_list[8].x > lm_list[6].x and lm_list[12].x < lm_list[10].x and \
                        lm_list[16].x < lm_list[14].x and lm_list[20].x < lm_list[18].x:
                    cv2.putText(img, "RIGHT", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                    print("RIGHT")
                    send_to_lcd("RIGHT", mode)
                    
                if all(finger_fold_status):
                    # Okay
                    if lm_list[thumb_tip].y < lm_list[thumb_tip - 1].y < lm_list[thumb_tip - 2].y and lm_list[0].x < \
                            lm_list[3].y:
                        print("OKAY")
                        send_to_lcd("OKAY", mode)
                        cv2.putText(img, "OKAY", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
                    # Disapprove
                    if lm_list[thumb_tip].y > lm_list[thumb_tip - 1].y > lm_list[thumb_tip - 2].y and lm_list[0].x < \
                            lm_list[3].y:
                        cv2.putText(img, "DISAPPROVE", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                        print("DISAPPROVE")
                        send_to_lcd("DISAPPROVE", mode)

                mp_draw.draw_landmarks(img, hand_landmark,
                                       mp_hands.HAND_CONNECTIONS,
                                       mp_draw.DrawingSpec((0, 0, 255), 6, 3),
                                       mp_draw.DrawingSpec((0, 255, 0), 4, 2)
                                       )

        cv2.imshow("Hand Sign Detection", img)
        cv2.waitKey(1)

