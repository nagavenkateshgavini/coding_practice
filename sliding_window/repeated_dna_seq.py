class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        storage = set()
        result = set()
        i, j = 0, 10
        while j <= len(s):
            seq = s[i:j]
            if seq not in storage:
                storage.add(seq)
            else:
                result.add(seq)
            i += 1
            j += 1
        
        return list(result)