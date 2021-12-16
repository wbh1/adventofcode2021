from solutions.Puzzle import Puzzle
import math


class Packet:
    def __init__(self, binary_string: str):
        self.index = 0
        self.subpackets = []

        self.binstr = binary_string

        self.VERSION = self.read_int(3)
        self.ID = self.read_int(3)

        # value of a packet is the value of its subpackets
        self.value = self.unwrap()

        self.vsum = self.VERSION
        for spkt in self.subpackets:
            self.vsum += spkt.vsum

    def _read(self, length):
        if self.index + length > len(self.binstr):
            raise Exception("you screwed up")
        ret = self.binstr[self.index : self.index + length]
        self.index += length
        return ret

    def read_int(self, length):
        return int(self._read(length), 2)

    def unwrap(self):
        if self.ID == 4:
            num = ""
            while True:
                header = self.read_int(1)
                num += self._read(4)
                if header == 0:
                    break
            return int(num, 2)
        else:
            return self.unwrap_subpackets()

    def unwrap_subpackets(self):
        ltid = self.read_int(1)

        if ltid == 0:
            subpkt_length = self.read_int(15)
            remaining_length = len(self.binstr[self.index :]) - subpkt_length
            while remaining_length != len(self.binstr[self.index :]):
                self.subpackets.append(Packet(self.binstr[self.index :]))
                self.index += self.subpackets[-1].index
        else:
            num_sub_pkts = self.read_int(11)
            for i in range(num_sub_pkts):
                self.subpackets.append(Packet(self.binstr[self.index :]))
                self.index += self.subpackets[-1].index

        subpkt_values = [pkt.value for pkt in self.subpackets]
        ID = self.ID
        # if there's only one value, skip the conditions
        if len(subpkt_values) == 1:
            return subpkt_values[0]

        if ID == 0:
            return sum(subpkt_values)
        elif ID == 1:
            return math.prod(subpkt_values)
        elif ID == 2:
            return min(subpkt_values)
        elif ID == 3:
            return max(subpkt_values)
        elif ID == 5:
            return 1 if subpkt_values[0] > subpkt_values[1] else 0
        elif ID == 6:
            return 1 if subpkt_values[0] < subpkt_values[1] else 0
        elif ID == 7:
            return 1 if subpkt_values[0] == subpkt_values[1] else 0


class Day16(Puzzle):
    def __init__(self, filename):
        with open(f"inputs/{filename}.txt") as f:
            # Zero pad 🤬
            data = "".join([bin(int(c, 16))[2:].zfill(4) for c in f.read().strip()])
        self.versions = 0
        self.data = data

    def part1(self) -> int:
        self.pkt = Packet(self.data)
        return self.pkt.vsum

    def part2(self) -> int:
        return self.pkt.value
