import cv2
import mediapipe as mp


class HandDetector:

    def __init__(self):

        self.results = None

        self.mpHands = mp.solutions.hands

        self.hands = self.mpHands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )

        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img):

        self.results = self.hands.process(
            cv2.cvtColor(
                img,
                cv2.COLOR_BGR2RGB
            )
        )

        if self.results and self.results.multi_hand_landmarks:

            for handLms in self.results.multi_hand_landmarks:

                self.mpDraw.draw_landmarks(
                    img,
                    handLms,
                    self.mpHands.HAND_CONNECTIONS
                )

                h, w, c = img.shape

                for id, lm in enumerate(handLms.landmark):

                    cx = int(lm.x * w)
                    cy = int(lm.y * h)

                    cv2.putText(
                        img,
                        str(id),
                        (cx, cy),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.5,
                        (255, 0, 0),
                        2
                    )

        return img
    def findPosition(self, img):

        lmList = []

        if self.results and self.results.multi_hand_landmarks:

            hand = self.results.multi_hand_landmarks[0]

            h, w, c = img.shape

            for id, lm in enumerate(hand.landmark):

                cx = int(lm.x * w)
                cy = int(lm.y * h)

                lmList.append(
                    [id, cx, cy]
                )

        return lmList