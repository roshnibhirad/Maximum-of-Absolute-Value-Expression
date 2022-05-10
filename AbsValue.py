class Solution:
    def maxAbsValExpr(self, a: List[int], b: List[int]) -> int:
        n = len(a)
        val = 0
        
        for x, y in product([-1,1], repeat=2):
            ival = (x*a[i] + y*b[i] + i for i in range(n))
            jval = (x*a[j] + y*b[j] + j for j in range(n))
            val = max(val, max(ival) - min(jval))
        
        return val