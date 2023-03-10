import cv2
import mediapipe as mp
import math
import copy
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
xvals = []
timecounter = 0
text = ""
persistence =  7
fontsize = 10
diff = 10

def dist(landmark1, landmark2):
    dist = 100 * math.sqrt((landmark1.x - landmark2.x)**2 + (landmark1.y - landmark2.y)**2)
    return dist

# For webcam input:
cap = cv2.VideoCapture(1)
with mp_hands.Hands(
        model_complexity=0,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            # If loading a video, use 'break' instead of 'continue'.
            continue

        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image)

        # Draw the hand annotations on the image.
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        cv2.rectangle(image, (100, 960), (1900, 850), (0,0,0), -1)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())
                TIP_1 = hand_landmarks.landmark[4]
                TIP_2 = hand_landmarks.landmark[8]
                TIP_3 = hand_landmarks.landmark[12]
                TIP_4 = hand_landmarks.landmark[16]
                TIP_5 = hand_landmarks.landmark[20]
                # if dist(TIP_1, TIP_2) > 25:
                #     print("Zoom in")
                # else:
                #     print("Nothing")

                # if dist(TIP_1, TIP_5) > 35:
                #     print("Pause")
                # else:
                #     print("No action")
                
                
                xvals.append(TIP_2.x) # change which finger is tracked
                if (len(xvals) < 10):
                    break
                elif xvals[-diff] == None or xvals[-1] == None:
                    break
                else:
                    if timecounter == 0:
                        if (xvals[-1] - xvals[-diff]) * 100 > 20:
                            image = cv2.flip(image, 1)
                            text = "GO BACK 5sec"
                            image = cv2.putText(image, text, (100,960), fontFace=1, fontScale=fontsize, thickness=10, color=(255,255,255))
                            image = cv2.flip(image, 1)
                        elif (xvals[-1] - xvals[-diff]) * 100 < -20:
                            image = cv2.flip(image, 1)
                            text = "GO FORWARD 5sec"
                            image = cv2.putText(image, text, (100,960), fontFace=1, fontScale=fontsize, thickness=10, color=(255,255,255))
                            image = cv2.flip(image, 1)
                        else:
                            text = " "
                            image = cv2.putText(image, text, (100,960), fontFace=1, fontScale=fontsize, thickness=10, color=(255,255,255))
                    else:
                        image = cv2.flip(image, 1)
                        image = cv2.putText(image, text, (100,960), fontFace=1, fontScale=fontsize, thickness=10, color=(255,255,255))
                        image = cv2.flip(image, 1)
                    timecounter += 1
                    timecounter %= persistence
                    
                    print((xvals[-1] - xvals[-diff]) * 100)
        else:
            xvals.append(None)
            if timecounter == 0:
                text = " "
                image = cv2.putText(image, text, (100,960), fontFace=1, fontScale=fontsize, thickness=10, color=(255,255,255))
            else:
                image = cv2.flip(image, 1)
                image = cv2.putText(image, text, (100,960), fontFace=1, fontScale=fontsize, thickness=10, color=(255,255,255))
                image = cv2.flip(image, 1)
            timecounter += 1
            timecounter %= persistence
        # Flip the image horizontally for a selfie-view display.
        cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
        # cv2.imshow('MediaPipe Hands', image)
        # Enter key 'q' to break the loop
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break
cap.release()
