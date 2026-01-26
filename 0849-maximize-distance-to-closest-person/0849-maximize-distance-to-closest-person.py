class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        maxDist = 0

        i = 0

        while i < n and seats[i] == 0:
            i += 1
        maxDist = i

        zeroCount = 0
        for j in range(i, n):
            if seats[j] == 0:
                zeroCount += 1
            else:
                maxDist = max(maxDist, (zeroCount + 1) // 2)
                zeroCount = 0
        
        maxDist = max(maxDist, zeroCount)

        return maxDist
        