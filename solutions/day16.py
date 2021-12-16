from solutions.Puzzle import Puzzle
import math


# Screw trying to do it a pretty way
VALS = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}


class Day16(Puzzle):
    def __init__(self, filename):
        with open(f"inputs/{filename}.txt") as f:
            data = f.read().strip()
        bin_string = ""
        for c in data:
            bin_string += VALS[c]
        data = bin_string
        self.versions = 0
        # data = bin(int("C0015000016115A2E0802F182340", 16))[2:]
        while len(data) % 4 != 0:
            data = "0" + data
        self.data = data

    def part1(self) -> int:
        self.value = self.read_packet()
        return self.versions

    def part2(self) -> int:
        return self.value

    def read(self, length):
        ret = self.data[:length]
        self.data = self.data[length:]
        return ret

    def read_packet(self):
        version = int(self.read(3), 2)
        ID = int(self.read(3), 2)

        self.versions += version

        if ID == 4:
            num = ""
            while True:
                chunk = self.read(5)
                num += chunk[1:]
                if chunk[0] == "0":
                    break
            return int(num, 2)

        length_type_id = int(self.read(1))

        subpkt_values = []
        if length_type_id == 0:
            subpkt_length = int(self.read(15), 2)
            remaining_len = len(self.data) - subpkt_length
            while remaining_len != len(self.data):
                subpkt_values.append(self.read_packet())
        else:
            num_sub_pkts = int(self.read(11), 2)
            subpkt_values = [self.read_packet() for i in range(num_sub_pkts)]

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
