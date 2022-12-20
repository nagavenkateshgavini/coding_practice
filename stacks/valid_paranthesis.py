from collections import deque

class Solution:

    def __init__(self):
        self.paranthesis_map = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        self.stack = deque()

    def isValid(self, s: str) -> bool:
        all_keys = self.paranthesis_map.keys()
        for char in s:
            if char in all_keys or len(self.stack) == 0:
                self.stack.append(char)
            else:
                last_ele = self.stack.pop()
                if self.paranthesis_map.get(last_ele) != char:
                    return False
        
        if len(self.stack) > 0:
            return False

        return True


if __name__ == "__main__":
	s = Solution()
	print(s.isValid("([])"))	
