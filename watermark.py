#!/usr/bin/env python3

"""
Simple script to overlay an image with a watermark image.

install pip in linux/*ubuntu:
sudo apt-get install python-pip
sudo apt-get install python3-pip

install pillow things:
http://pillow.readthedocs.io/en/latest/installation.html#linux-installation
sudo apt-get install python-imaging


"""

import sys
import os
import argparse

from PIL import Image


class SimpleWatermark(object):
    """Simple Wartermark adding."""

    def __init__(self, input_filename, output_filename, watermark_filename):
        """Init instance."""
        super(SimpleWatermark, self).__init__()

        self.input_filename = input_filename
        self.output_filename = output_filename
        self.watermark_filename = watermark_filename

        self.img_in = None
        self.img_wm = None

    def __del__(self):
        """Clean up."""
        try:
            self.img_in.close()
        except Exception as e:
            print(e)
        try:
            self.img_wm.close()
        except Exception as e:
            print(e)

    def load(self):
        """Load Images from files."""
        self.img_in = Image.open(self.input_filename)
        print("img_in", self.img_in.format, self.img_in.size, self.img_in.mode)

        self.img_wm = Image.open(self.watermark_filename)
        print("img_wm", self.img_wm.format, self.img_wm.size, self.img_wm.mode)

    def show(self):
        """
        Debugging helper.

        http://pillow.readthedocs.io/en/latest/handbook/tutorial.html#using-the-image-class
        """
        self.img_in.show()
        self.img_wm.show()

    def process(self):
        """Process."""
        in_width, in_height = self.img_in.size
        wm_width, wm_height = self.img_wm.size

        # define box as in the bottom right corner
        #  (left, upper, right, lower).
        box = (
            in_width - wm_width,
            in_height - wm_height,
            in_width,
            in_height
        )

        self.img_in.paste(self.img_wm, box=box, mask=self.img_wm)

    def save(self):
        """Save Image to file."""
        self.img_in.save(self.output_filename)


def main():
    """Main SW."""
    print(42*'*')
    print('Python Version: ' + sys.version)
    print(42*'*')

    input_filename_default = "./image1.png"
    output_filename_default = "./image1_wm.png"
    watermark_filename_default = "./mark.png"

    parser = argparse.ArgumentParser(
        description="adds watermark to image file."
    )

    parser.add_argument(
        "-i",
        "--input_filename",
        help="specify a location for the input file (defaults to {})".format(
            input_filename_default
        ),
        metavar='INPUT_FILENAME',
        default=input_filename_default
    )
    parser.add_argument(
        "-o",
        "--output_filename",
        help="specify a location for the output file (defaults to {})".format(
            output_filename_default
        ),
        metavar='OUTPUT_FILENAME',
        default=output_filename_default
    )
    parser.add_argument(
        "-w",
        "--watermark_filename",
        help=(
            "specify a location for the watermark file "
            "(defaults to {})"
        ).format(
            watermark_filename_default
        ),
        metavar='WATERMARK_FILENAME',
        default=watermark_filename_default
    )
    args = parser.parse_args()

    myMark = SimpleWatermark(
        input_filename=args.input_filename,
        output_filename=args.output_filename,
        watermark_filename=args.watermark_filename
    )
    myMark.load()
    # myMark.show()
    myMark.process()
    myMark.save()


if __name__ == "__main__":
    main()
