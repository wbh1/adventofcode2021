import heapq
from collections import defaultdict
from math import inf

from solutions.Puzzle import Puzzle

# delta row / delta column
# right, left, up, down (respectively)
DR = [0, 0, -1, 1]
DC = [1, -1, 0, 0]


class Day15(Puzzle):
    def __init__(self, filename):
        with open(f"inputs/{filename}.txt") as f:
            data = [line for line in f.read().splitlines()]
            self.data = [[int(n) for n in line] for line in data]

    def dijkstra(self):
        # Bottom right corner
        DEST_X, DEST_Y = len(self.data) - 1, len(self.data[0]) - 1

        # Initialize queue as list of tuples
        # with format: (distance_from_start, (x, y))
        queue = [(0, (0, 0))]
        visited = set()

        # defaultdict takes a function for specifying default values
        # djikstra's specifies that each node's distance from the start
        # is always presumed to be infinity initally
        mindist = defaultdict(lambda: inf, {(0, 0): 0})

        while queue:
            # heapq (i.e. priority queue) helps explore the paths
            # that currently have the lowest weights first, before branching
            # off to other paths.
            dist, node = heapq.heappop(queue)

            # we arrived!
            if node == (DEST_X, DEST_Y):
                return dist

            # Gandalf may have no memory of this place, but I do
            if node in visited:
                continue

            visited.add(node)
            x, y = node

            for neighbor in self.neighbors(node):
                nx, ny = neighbor
                # add the risk for the neighbor
                newdist = dist + self.data[ny][nx]

                # if the newdistance is less than the currently known
                # min distance for reaching this point, then update it
                # and mark it for future exploration
                #
                # We don't need to keep track of what point we came through
                # in order to achieve that min distance, though -- just
                # the minimum distance needed to get there.
                if newdist < mindist[neighbor]:
                    mindist[neighbor] = newdist
                    heapq.heappush(queue, (newdist, neighbor))

        return "you suck"

    def part1(self) -> int:
        return self.dijkstra()

    def part2(self) -> int:
        tile_width = len(self.data[0])
        tile_height = len(self.data)

        # make the row longer
        for _ in range(4):
            for row in self.data:
                # rewind to start of tile
                tail = row[-tile_width:]
                row.extend((x + 1) if x < 9 else 1 for x in tail)

        # make more rows
        for _ in range(4):
            for row in self.data[-tile_height:]:
                row = [(x + 1) if x < 9 else 1 for x in row]
                self.data.append(row)

        return self.dijkstra()

    def neighbors(self, point: tuple):
        x, y = point
        opts = []
        for i in range(0, 4):
            if 0 <= y + DR[i] < len(self.data) and 0 <= x + DC[i] < len(self.data[0]):
                opts.append((x + DC[i], y + DR[i]))
        return opts
