class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        power = list(enumerate([sum(x) for x in mat]))
        power.sort(key=lambda x:x[1])

        return [x[0] for x in power[:k]]