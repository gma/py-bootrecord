class MalformedEntryError(StandardError):

    pass


class Partition(object):

    def __init__(self, hex_codes):
        if len(hex_codes) == 16:
            self.is_bootable = hex_codes[0] == '80'
        else:
            raise MalformedEntryError
