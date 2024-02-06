import collections

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        answer = 0
        stonecount = collections.Counter(stones)
        for i in jewels:
            answer += stonecount[i]
        return answer