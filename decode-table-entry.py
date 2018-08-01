#!/usr/bin/env python

import sys


def hex_to_int(hex_string):
    return int(hex_string, 16)


def split_second_byte(hex_string):
    value = hex_to_int(hex_string)
    return value & 0b00111111, value & 0b11000000


def convert_to_lba_address(cylinder, head, sector):
    num_heads = 255
    sectors_per_track = 63
    return ((cylinder * num_heads) + head) * sectors_per_track + sector


def main(head, byte2, byte3):
    head = hex_to_int(head)
    sector, cylinder = split_second_byte(byte2)
    cylinder = cylinder + hex_to_int(byte3)

    address = convert_to_lba_address(cylinder, head, sector)

    print "CHS: %s, %s, %s => %s" % (cylinder, head, sector, address)


if __name__ == '__main__':
    main(*sys.argv[1:])
