import collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countnums = collections.Counter(nums)
        answer = [key for key, _ in countnums.most_common(k)]
        
        return answer