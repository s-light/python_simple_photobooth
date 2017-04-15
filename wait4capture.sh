# Aktivierung des Tethering-Modus der Kamera und Warten auf Bilder
# gphoto2 --capture-tethered --filename="../captured/photo_booth-%Y%m%d-%H%M%S.%C" --force-overwrite
# gphoto2 --capture-tethered --hook-script=gphoto2_script_hook_handler.py --filename="../captured/photo_booth-%Y%m%d-%H%M%S.%C" --force-overwrite
gphoto2 --capture-tethered --hook-script=photobooth_handler.py --filename="../captured/photo_booth-%Y%m%d-%H%M%S.%C" --force-overwrite
