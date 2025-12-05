class Solution:
    def countCollisions(self, directions):
        s = directions.lstrip("L").rstrip("R")
        count = 0
        for c in s:
            if c == "R" or c == "L":
                count += 1
        return count