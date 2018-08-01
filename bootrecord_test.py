import unittest

import bootrecord as br


class PartitionTest(unittest.TestCase):

    bootable = '80 01 01 00 0B 1F 3F 33 3F 00 00 00 41 99 01 00'.split()
    unbootable = '00 00 c1 6e 0c fe ff ff ee 39 d7 00 bd 86 bb 00'.split()

    def test_requires_16_bytes(self):
        self.assertRaises(br.MalformedEntryError, br.Partition, ['00'])
        br.Partition(self.bootable)

    def test_extracts_bootable_flag(self):
        self.assertTrue(br.Partition(self.bootable).is_bootable)
        self.assertFalse(br.Partition(self.unbootable).is_bootable)


if __name__ == '__main__':
    unittest.main()
