#solve withour sorting

import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        new_nums = [-x for x in nums]
        heapq.heapify(new_nums)
        for _ in range(k):
            answer = -heapq.heappop(new_nums)
        return answer
