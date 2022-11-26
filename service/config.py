import sys

from service import log

config_map = {}


def create_config():
    config_map["cascPath"] = "input/cascade/haarcascade_frontalface_default.xml"
    if len(sys.argv) > 1:
        config_map["output"] = sys.argv[1]
    else:
        config_map["output"] = "file"

    if len(sys.argv) > 2:
        config_map["output_img_path"] = sys.argv[2]
    else:
        config_map["output_img_path"] = "output/frame"

    if len(sys.argv) > 3:
        config_map["output_video_path"] = sys.argv[2]
    else:
        config_map["output_video_path"] = "output/video"

    log.info("casc set to be "+config_map["cascPath"])
    log.info("output set to be " + config_map["output"])
    log.info("output img path set to be " + config_map["output_img_path"])
    log.info("output video path set to be " + config_map["output_video_path"])

    pass
