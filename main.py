import cv2
from hand_detector import HandDetector

cap = cv2.VideoCapture(0)

detector = HandDetector()

tipIds = [4, 8, 12, 16, 20]

while True:

    success, img = cap.read()

    img = detector.findHands(img)

    lmList = detector.findPosition(img)

    if len(lmList) != 0:

        fingers = []

        # Thumb
        if lmList[4][1] > lmList[3][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        # Other 4 fingers
        for id in range(1, 5):

            if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        count = sum(fingers)

        cv2.rectangle(
            img,
            (20, 20),
            (170, 120),
            (0, 255, 0),
            cv2.FILLED
        )

        cv2.putText(
            img,
            str(count),
            (50, 100),
            cv2.FONT_HERSHEY_SIMPLEX,
            3,
            (255, 255, 255),
            5
        )

    cv2.imshow(
        "Finger Counter",
        img
    )

    key = cv2.waitKey(1)

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()