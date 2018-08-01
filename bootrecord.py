class MalformedEntryError(StandardError):

    pass


def hex_to_int(hex_code):
    return int(hex_code, 16)


class TableEntry(object):

    def __init__(self, hex_codes):
        sector, cylinder = self.split_second_byte(hex_to_int(hex_codes[1]))
        self.cylinder = cylinder + hex_to_int(hex_codes[2])

    def split_second_byte(self, value):
        # The middle byte stores both the sector and some of the
        # cylinder (the rest of which is in the third byte). We need
        # to extract the relevant parts of the byte, as follows...
        sector_mask = 0b00111111
        cylinder_mask = 0b11000000
        return value & sector_mask, value & cylinder_mask


class Partition(object):

    def __init__(self, hex_codes):
        if len(hex_codes) == 16:
            self.is_bootable = hex_codes[0] == '80'
        else:
            raise MalformedEntryError
