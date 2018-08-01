#!/usr/bin/env python

import sys


def hex_to_int(hex_string):
    return int(hex_string, 16)


def split_second_byte(hex_string):
    value = hex_to_int(hex_string)
    return value & 0b00111111, value & 0b11000000


def convert_chs_bytes(*hex_strings):
    head = hex_to_int(hex_strings[0])
    sector, cylinder = split_second_byte(hex_strings[1])
    cylinder = cylinder + hex_to_int(hex_strings[2])


def convert_to_lba_address(cylinder, head, sector):
    num_heads = 255
    sectors_per_track = 63
    return ((cylinder * num_heads) + head) * sectors_per_track + sector - 1


def main(hex_codes):
    bootable = hex_codes[0]
    start_chs = hex_codes[1:4]
    partition_type = hex_codes[4]
    end_chs = hex_codes[5:8]
    starting_sector = hex_codes[8:12]
    partition_size = hex_codes[12:16]

    print "Bootable: %s [80 indicates bootable]" % bootable
    print start_chs

    #  sector, cylinder = split_second_byte(byte2)
    #  cylinder = cylinder + hex_to_int(byte3)

    #  address = convert_to_lba_address(cylinder, head, sector)

    #  print "CHS: %s, %s, %s => %s" % (cylinder, head, sector, address)


if __name__ == '__main__':
    main(sys.argv[1:])
