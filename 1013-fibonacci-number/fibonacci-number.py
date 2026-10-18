
class Solution:
    def rec(self, n, dp):
        # Base case
        if n == 0 or n == 1:
            return n

        # Return cached result
        if dp[n] != -1:
            return dp[n]

        # Recursive case
        dp[n] = self.rec(n - 1, dp) + self.rec(n - 2, dp)
        return dp[n]

    def fib(self, n: int) -> int:
        dp = [-1] * (n + 1)
        return self.rec(n, dp)
