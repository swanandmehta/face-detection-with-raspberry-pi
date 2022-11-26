import time
import cv2
import os

from service import config, log, video
from service.config import config_map


def init():
    if not os.path.exists(config_map["output_img_path"]):
        os.makedirs(config_map["output_img_path"])

    fps_limit = 1
    start_time = time.time()
    face_cascade = cv2.CascadeClassifier(config.config_map["cascPath"])
    video_capture = cv2.VideoCapture(0)

    while True:
        now_time = time.time()
        if (int(now_time - start_time)) < fps_limit:
            continue

        start_time = time.time()

        ret, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        log.info("Found {0} faces!".format(len(faces)))

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, "Person", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))

        cv2.imwrite(config_map["output_img_path"] + "/" + str(int(time.time())) + ".png", frame)
        video.init()

    video_capture.release()
    cv2.destroyAllWindows()
    pass

