#!/usr/bin/env python3
from PIL import Image
import numpy
import sys
import pathlib

"""
Takes a 250x122 pixel 8-bit PNG image and 
converts it into a .bin for display on inky:bit.

Use with: inkybit.draw_bin("filename.bin")
"""

COLS = 136
ROWS = 250

if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} image.png")
    sys.exit(1)

filename = pathlib.Path(sys.argv[1])

source = Image.open(filename)

if source.size != (250, 122):
    print(f"Image must be 250x122 pixels!")
    sys.exit(1)

image = Image.new("P", (ROWS, COLS), 1)

image.paste(source, (0, 6))

image.putpalette(source.getpalette())
image = image.rotate(-90, expand=True)

pixels = numpy.array(list(image.tobytes()))

buf_a = numpy.packbits(pixels == 0).tobytes()
buf_b = numpy.packbits(pixels == 2).tobytes()

out_filename = filename.with_suffix(".bin")
print(f"Saving as {out_filename}")
with open(out_filename, "wb") as f:
    f.write(buf_a + buf_b)