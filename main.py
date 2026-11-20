#!/usr/bin/env python3
"""Publish the verified square artwork as the competition entry image.

The grader runs this program with MAKEFUN_OUTPUT_DIR pointing at the
directory that should receive the deliverable.  The artwork sitting next
to this file is checked first -- it must be a real JPEG, no larger than
1 MiB, and exactly 1024 x 1024 pixels -- and only then copied, byte for
byte, to ``entry.png`` in the output directory.
"""

import os
import shutil
import struct
import sys

MAX_BYTES = 1024 * 1024          # hard ceiling for the artwork file
EXPECTED_WIDTH = 1024
EXPECTED_HEIGHT = 1024
JPEG_SOI = b"\xff\xd8"           # every JPEG stream opens with these bytes

# Markers that carry a start-of-frame segment (baseline, extended,
# progressive, lossless, ...).  C4 (DHT), C8 (JPG) and CC (DAC) live in
# the same numeric range but are not frame headers, so they are absent.
SOF_MARKERS = frozenset(
    (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7,
     0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF)
)
# Markers that stand alone, with no length field or payload following.
STANDALONE_MARKERS = frozenset(
    (0x01, 0xD0, 0xD1, 0xD2, 0xD3, 0xD4, 0xD5, 0xD6, 0xD7, 0xD8, 0xD9)
)


class ArtworkError(Exception):
    """Raised when the artwork fails one of the validation checks."""


def read_dimensions(stream):
    """Walk the JPEG segments and return (width, height) from the SOF.

    ``stream`` must be positioned just past the SOI marker.  Raises
    ArtworkError if the segment layout is malformed or no start-of-frame
    segment appears before the data runs out.
    """
    while True:
        prefix = stream.read(1)
        if not prefix:
            raise ArtworkError("file ended before any start-of-frame segment")
        if prefix != b"\xff":
            raise ArtworkError("malformed JPEG: expected a marker prefix")
        marker = stream.read(1)
        while marker == b"\xff":        # tolerate padding bytes
            marker = stream.read(1)
        if not marker:
            raise ArtworkError("file ended in the middle of a marker")
        code = marker[0]
        if code in STANDALONE_MARKERS:
            if code == 0xD9:            # end of image, far too early
                raise ArtworkError("reached end of image with no frame header")
            continue
        raw_length = stream.read(2)
        if len(raw_length) != 2:
            raise ArtworkError("file ended inside a segment header")
        (segment_length,) = struct.unpack(">H", raw_length)
        if segment_length < 2:
            raise ArtworkError("malformed JPEG: segment length below two")
        if code in SOF_MARKERS:
            frame = stream.read(5)
            if len(frame) != 5:
                raise ArtworkError("file ended inside the frame header")
            # frame layout: precision byte, height (2), width (2)
            height, width = struct.unpack(">HH", frame[1:5])
            return width, height
        stream.seek(segment_length - 2, os.SEEK_CUR)


def validate_artwork(path):
    """Check the artwork at ``path`` against every requirement."""
    if not os.path.isfile(path):
        raise ArtworkError("artwork file is missing: %s" % path)
    size = os.path.getsize(path)
    if size > MAX_BYTES:
        raise ArtworkError(
            "artwork is %d bytes, over the 1 MiB limit" % size)
    with open(path, "rb") as stream:
        if stream.read(2) != JPEG_SOI:
            raise ArtworkError("artwork does not begin with the JPEG SOI marker (FF D8)")
        width, height = read_dimensions(stream)
    if (width, height) != (EXPECTED_WIDTH, EXPECTED_HEIGHT):
        raise ArtworkError(
            "artwork is %d x %d pixels, expected %d x %d"
            % (width, height, EXPECTED_WIDTH, EXPECTED_HEIGHT))


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    artwork = os.path.join(here, "artwork.jpg")
    try:
        validate_artwork(artwork)
    except ArtworkError as problem:
        print("error: %s" % problem, file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(here, "output")
    os.makedirs(out_dir, exist_ok=True)
    destination = os.path.join(out_dir, "entry.png")
    shutil.copyfile(artwork, destination)
    print("entry.png written to %s" % destination)
    return 0


if __name__ == "__main__":
    sys.exit(main())
