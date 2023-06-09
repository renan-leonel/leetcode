class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, number in enumerate(nums):
            difference = target - number
            if difference in hashmap:
                return [index, hashmap[difference]]
            hashmap[number] = index