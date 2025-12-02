class Solution(object):
    def countTrapezoids(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7
        
        # Group points by y-coordinate
        y_groups = {}
        for x, y in points:
            if y not in y_groups:
                y_groups[y] = []
            y_groups[y].append(x)
        
        # Get all y-coordinates
        y_coords = list(y_groups.keys())
        n = len(y_coords)
        
        count = 0
        
        # For each pair of different y-coordinates
        for i in range(n):
            for j in range(i + 1, n):
                y1, y2 = y_coords[i], y_coords[j]
                n1 = len(y_groups[y1])
                n2 = len(y_groups[y2])
                
                # Number of ways to choose 2 points from each level
                # C(n1, 2) * C(n2, 2)
                if n1 >= 2 and n2 >= 2:
                    ways1 = n1 * (n1 - 1) // 2
                    ways2 = n2 * (n2 - 1) // 2
                    count = (count + ways1 * ways2) % MOD
        
        return count