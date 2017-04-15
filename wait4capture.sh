# activate gphoto2

gphoto2 --capture-tethered --hook-script=photobooth_handler.py --filename="./captured/photo_booth-%Y%m%d-%H%M%S.%C" --force-overwrite
