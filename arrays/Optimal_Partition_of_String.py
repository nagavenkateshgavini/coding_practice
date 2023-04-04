class Solution:
    def partitionString(self, s: str) -> int:
        _set = set()
        res = 1
        for i in range(len(s)):
            if s[i] in _set:
                res += 1
                _set = set()
            _set.add(s[i])
            
        return res

    
if __name__ == "__main__":
    s = Solution()
    c = s.partitionString("cuieokbs")
    print(c)
    