class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        _d = {}
        for idx, num in enumerate(nums):
            diff = target - num
            diff_idx = _d.get(diff, None)
            if isinstance(diff_idx, int):
                return [idx, diff_idx]
            _d[num] = idx