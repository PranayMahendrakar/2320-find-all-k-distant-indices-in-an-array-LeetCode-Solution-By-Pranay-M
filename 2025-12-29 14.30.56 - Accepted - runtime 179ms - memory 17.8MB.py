class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        # Find all indices j where nums[j] == key
        key_indices = [j for j in range(len(nums)) if nums[j] == key]
        
        # Find all k-distant indices
        result = set()
        for j in key_indices:
            for i in range(max(0, j - k), min(len(nums), j + k + 1)):
                result.add(i)
        
        return sorted(result)