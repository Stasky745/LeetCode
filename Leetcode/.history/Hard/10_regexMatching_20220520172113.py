import time

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s, p = ' '+ s, ' '+ p
        lenS, lenP = len(s), len(p)
        dp = [[False]*(lenP) for i in range(lenS)]
        dp[0][0] = True

        for j in range(1, lenP):
            if p[j] == '*':
                dp[0][j] = dp[0][j-2]

        for i in range(1, lenS):
            for j in range(1, lenP):
                if p[j] in {s[i], '.'}:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j] == "*":
                    dp[i][j] = dp[i][j-2] or int(dp[i-1][j] and p[j-1] in {s[i], '.'})

        return dp[-1][-1]
    
# Program
s1 = "aa"
p1 = "a"

s2 = "aa"
p2 = "a*"

s3 = "ab"
p3 = ".*"

t0 = time.perf_counter_ns()

s = Solution()

print(s.isMatch(s1, p1))
print(s.isMatch(s2, p2))
print(s.isMatch(s3, p3))

t1 = time.perf_counter_ns()

print(f"{(t1-t0)/1000000} ms.")    