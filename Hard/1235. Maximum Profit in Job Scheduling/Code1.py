class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        st = [(startTime[i],i) for i in range(n)]
        st.sort()

        dp = [0]*(n+1)
        for i in range(n-1,-1,-1):
            next_profit = bisect.bisect_left(st,(endTime[st[i][1]],0),i+1)
            dp[i] = max(dp[i+1],profit[st[i][1]]+dp[next_profit])
        return dp[0]
