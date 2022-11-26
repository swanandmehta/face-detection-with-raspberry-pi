import os
import time

import cv2
import glob

from service.config import config_map


def init():
    if not os.path.exists(config_map["output_video_path"]):
        os.makedirs(config_map["output_video_path"])

    frame_limit_per_video = 60

    files = glob.glob(config_map["output_img_path"] + "/*.png")

    if len(files) > frame_limit_per_video:
        size = (600, 600)
        fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
        out = cv2.VideoWriter(config_map["output_video_path"] + "/" + str(int(time.time())) + ".avi", fourcc, 5, size, isColor=True)

        for img_name in files:
            img = cv2.imread(img_name)
            img = cv2.resize(img, size)
            out.write(img)

        out.release()

        for img_name in files:
            os.remove(img_name)