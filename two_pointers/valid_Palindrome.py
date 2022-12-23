import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub("[^a-zA-Z0-9\n]", "", s)

        #s = list(filter(lambda ch: ch.isalnum(), s))
        #s = list(map(lambda ch: ch.lower(), s))


        start = 0
        end = len(s) - 1
        while(start < end):
            start_char = s[start]
            end_char = s[end]
            if start_char == end_char:
                start += 1
                end -= 1
            else:
                return False
        
        return True

if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome("A man, a plan, a canal: Panama"))
