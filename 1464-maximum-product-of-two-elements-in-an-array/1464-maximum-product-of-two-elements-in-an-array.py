import heapq
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        new_nums =[-x for x in nums]
        heapq.heapify(new_nums)
        
        a = -heapq.heappop(new_nums)
        b = -heapq.heappop(new_nums)

        return (a-1) * (b-1)