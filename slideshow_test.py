#!/usr/bin/env python3

"""
Slideshow test.

just tests..
"""

import sys
import os
import subprocess
from contextlib import contextmanager

##########################################
# functions

@contextmanager
def cd(newdir):
    """
    Change directory.

    found at:
    http://stackoverflow.com/questions/431684/how-do-i-cd-in-python/24176022#24176022
    """
    prevdir = os.getcwd()
    os.chdir(os.path.expanduser(newdir))
    try:
        yield
    finally:
        os.chdir(prevdir)


##########################################
# classes

class PhotoBoothHandler():
    """docstring for PhotoBoothHandler."""

    def __init__(self):
        """Initialize Instance."""
        # print("PhotoBoothHandler")
        self.path_script = os.path.dirname(os.path.abspath(__file__))
        print("path_script", self.path_script)

        super(PhotoBoothHandler, self).__init__()

    def __del__(self):
        """Clean up."""
        pass

    def start(self, argument):
        """gPhoto2 started."""
        self.start_slideshow()

    def stop(self, argument):
        """gPhoto2 started."""
        self.stop_slideshow()

    def stop_slideshow(self):
        """Stop Slideshow."""
        print("stop slideshow:")
        command = [
            "killall",
            "feh",
        ]
        result_string = ""
        try:
            # print("command:{}".format(" ".join(command)))
            result_string += subprocess.check_output(command).decode()
        except subprocess.CalledProcessError as e:
            error_message = "failed: {}".format(e)
            print(error_message)
            result_string += "\n" + error_message
        else:
            pass
        return result_string

    def start_slideshow(self, startfile=None):
        """Restart Slideshow."""
        print("start slideshow:")
        duration_new_picture = 5.0
        duration_loop = 1.0

        target_path = self.path_script
        image_directory = "./captured/"
        # image_directory = "./"

        # https://man.finalrewind.org/1/feh/
        command_start = [
            "feh",
            "--fullscreen",
            "--cycle-once",
            "--slideshow-delay={}".format(duration_new_picture),
            "{}".format(startfile),
        ]
        command_loop = [
            "feh",
            "--fullscreen",
            "--randomize",
            "--slideshow-delay={}".format(duration_loop),
            "{}".format(image_directory),
        ]
        # command_loop = [
        #     "feh",
        #     "--fullscreen",
        #     "--randomize",
        #     "--slideshow-delay=1",
        #     "./captured/",
        # ]

        command = []

        # if startfile:
        #     command.extend(command_start)
        #     command.append("&&")
        #     command.extend(command_loop)
        # else:
        #    command = command_loop
        command = command_loop

        result_string = ""
        try:
            print("command:{}".format(" ".join(command)))
            with cd(target_path):
                # result_string += subprocess.check_output(command).decode()
                # this does not work with the && combining of commands..
                # subprocess.Popen(command)
                # subprocess.Popen(command, shell=True)
                # command = " ".join(command)
                # subprocess.Popen(command, shell=True)
                # result_string += subprocess.check_output(command).decode()
                # subprocess.run(command, shell=True, check=True)
                subprocess.run(command)
        except subprocess.CalledProcessError as e:
            error_message = "failed: {}".format(e)
            print(error_message)
            result_string += "\n" + error_message
        else:
            pass
        return result_string


##########################################
# globals

myPBHandler = None


##########################################
# main

def main():
    """Main SW."""
    global myPBHandler
    myPBHandler = PhotoBoothHandler()
    myPBHandler.start_slideshow()


if __name__ == "__main__":
    main()
