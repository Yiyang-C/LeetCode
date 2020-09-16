class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        self.helper('', n, k, res)
        return res
        
    def helper(self, combo, remain, k, res):
        # print(combo)
        if len(combo) == k:
            if not remain:
                res.append(combo)
            return
        # elif not remain:
        #     return
        if combo:
            for num in range(int(combo[-1])+1, min(10, remain+1)):
                self.helper(combo+str(num), remain - num, k, res)
        else:
            for num in range(1, min(10, remain+1)):
                self.helper(combo+str(num), remain - num, k, res)
