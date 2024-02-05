class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()
        for i in range(len(nums) -2):
            # 중복 방지
            if i >0 and nums[i] == nums[i-1]:
                continue
            # 투 포인터 기법
            left, right = i+1, len(nums)-1
            while left < right:
                if nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    answer.append([nums[i], nums[left],nums[right]])
                    # 중복 방지
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left +=1
                    right -= 1
        return(answer)
        