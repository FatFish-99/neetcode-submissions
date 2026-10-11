class Solution:
    def climbStairs(self, n: int) -> int:
        prev, cur = 0, 0
        if n<=2:
            return n
        prev, cur = 1, 2
        for i in range(3, n+1):
            prev, cur = cur, cur+prev
        return cur
