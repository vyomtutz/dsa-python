nums = [3,4,5,6]

target = 9
lst = []
flag = False
# Brute Force approach to find pairs that sum up to the target
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Iterate through each number in the list
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                # Check if the sum of the two numbers equals the target
                if nums[i] + nums[j] == target:
                    # If a pair is found, return their indices
                    return [i, j]
        # If no pair is found, return an empty list
        return []