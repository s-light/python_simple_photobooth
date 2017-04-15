#!/usr/bin/env python3

"""
gphoto2 hook-script handler.

http://www.gphoto.com/doc/manual/ref-gphoto2-cli.html

install pip in linux/*ubuntu:
    sudo apt-get install python-pip
    sudo apt-get install python3-pip

install gphoto2 things:
    sudo apt-get install libgphoto2-dev
    sudo apt-get install gphoto2
    sudo apt-get install entangle
    (gui tool to test if camera connection and picture taking works.)
    # not needed
    sudo -H pip3 install -v gphoto2
    (https://pypi.python.org/pypi/gphoto2/1.5.1)

"""

import sys
import os
# import argparse


class Gphoto2HookScriptHandler(object):
    """docstring for Gphoto2HookScriptHandler."""

    def __init__(self):
        """Initialize Instance."""
        print("PhotoBoothHandler")
        super(Gphoto2HookScriptHandler, self).__init__()
        # self.arg = arg
        if 'ACTION' in os.environ:
            action = os.environ['ACTION']
            argument = None
            if 'ARGUMENT' in os.environ:
                argument = os.environ['ARGUMENT']

            if action.startswith("init"):
                self.init(argument)
            elif action.startswith("start"):
                self.start(argument)
            elif action.startswith("download"):
                self.download(argument)
            elif action.startswith("stop"):
                self.stop(argument)
            else:
                print("ACTION:", action)

    def init(self, argument):
        """Gphoto2 Init."""
        print("gphoto2 init")
        print(42*'*')
        print('Python Version: ' + sys.version)
        print(42*'*')

    def start(self, argument):
        """Gphoto2 Started."""
        print("gphoto2 start")
        if argument:
            print("argument:", argument)

    def stop(self, argument):
        """Gphoto2 Stopped."""
        print("gphoto2 stop")
        if argument:
            print("argument:", argument)

    def download(self, argument):
        """Gphoto2 Started."""
        print("gphoto2 donwload")
        if argument:
            print("argument:", argument)


def main():
    """Main SW."""
    Gphoto2HookScriptHandler()

    # parser = argparse.ArgumentParser(
    #     description="handle gphoto2 hook-script calls"
    # )
    # only use args after script name
    # args = sys.argv[1:]
    # args = sys.argv
    # print("args", args)
    # print("os.environ", os.environ)


if __name__ == "__main__":
    main()
