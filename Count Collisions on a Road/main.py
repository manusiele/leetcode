class Solution(object):
    def countCollisions(self, directions):
        """
        :type directions: str
        :rtype: int
        """
        stack = []
        collisions = 0
        for car in directions:
            if car == 'R':
                stack.append(car)
            elif car == 'S':
                stack.append(car)
            elif car == 'L':
                collided = False
                while stack and (stack[-1] == 'R' or stack[-1] == 'S'):
                    if stack[-1] == 'R':
                        collisions += 2
                    else:
                        collisions += 1
                    stack.pop()
                    collided = True
                if not collided:
                    stack.append(car)
        return collisions