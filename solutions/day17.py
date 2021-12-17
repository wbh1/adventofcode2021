from solutions.Puzzle import Puzzle

# Do yourself a favor and use pypy to run this
# It's brute force and not fast
class Day17(Puzzle):
    def __init__(self, test):
        if "test" in test:
            self.minX, self.maxX = (20, 30)
            self.minY, self.maxY = (-10, -5)
        else:
            self.minX, self.maxX = (217, 240)
            self.minY, self.maxY = (-126, -69)

        self.velocity = (0, 0)
        self.highest_y = 0
        self.working_velocities = set()
        self.p2 = 0

    def part1(self) -> int:
        for X_VELOCITY in range(250):
            for Y_VELOCITY in range(-150, 1000):
                peak = 0
                x, y = (0, 0)
                x_vel, y_vel = (X_VELOCITY, Y_VELOCITY)
                OK = False
                for step in range(1000):
                    x += x_vel
                    y += y_vel
                    peak = max(peak, y)
                    if x_vel > 0:
                        x_vel -= 1
                    elif x_vel < 0:
                        x_vel += 1
                    y_vel -= 1

                    if self.minX <= x <= self.maxX and self.minY <= y <= self.maxY:
                        OK = True
                if OK:
                    self.highest_y = max(self.highest_y, peak)
                    self.working_velocities.add((X_VELOCITY, Y_VELOCITY))
        return self.highest_y

    def part2(self) -> int:
        return len(self.working_velocities)
