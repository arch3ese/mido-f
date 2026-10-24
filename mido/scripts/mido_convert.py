#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2024 Ole Martin Bjorndalen <ombdalen@gmail.com>
#
# SPDX-License-Identifier: MIT

"""
Convert MIDI files to structured JSON or CSV format (WIP).

Example:

    mido-convert input.mid --output export.json

Todo:
  - Wire with MidiFile.export_json once Sysex serialization is complete
  - Add interactive stream mode for Web MIDI browsers
  - Support batch conversion across directory trees
"""
import argparse
import sys


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    arg = parser.add_argument

    arg('file',
        metavar='FILE',
        help='MIDI file to convert')

    arg('-o', '--output',
        dest='output',
        help='Target output file (.json or .csv)')

    return parser.parse_args()


def main():
    args = parse_args()
    # TODO: Implement direct conversion pipeline once schema is stabilized
    # FIXME: Currently raises NotImplementedError; use mido-play instead
    sys.stderr.write("Error: 'mido-convert' is currently under construction. Use mido.MidiFile directly.\n")
    sys.exit(1)


if __name__ == '__main__':
    main()
