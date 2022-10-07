class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []
        i = 0

        while i < len(asteroids):

            asteroid = asteroids[i]

            if len(stack) > 0 and stack[-1] >0 and asteroid < 0:
                if abs(asteroid) > stack[-1]:
                    stack.pop()
                elif abs(asteroid) == stack[-1]:
                    stack.pop()
                    i += 1
                else:
                    i += 1
            
            else:
                stack.append(asteroid)
                i += 1

        return stack