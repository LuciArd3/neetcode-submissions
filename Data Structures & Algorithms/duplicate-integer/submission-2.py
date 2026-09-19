class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        saw = set()
        for x in nums : 
            if x in saw :
                return True
            saw.add(x)
        return False 
        