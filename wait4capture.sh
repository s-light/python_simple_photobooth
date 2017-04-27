
# optional stop gphotofs related things.
# this is needed for raspberrypi to free up access to the camera
killall gvfsd-gphoto2

# activate gphoto2
gphoto2 \
    --capture-tethered \
    --hook-script=photobooth_handler.py \
    --filename="./captured/photo_booth-%Y%m%d-%H%M%S.%C" \
    --force-overwrite
