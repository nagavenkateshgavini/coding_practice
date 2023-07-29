class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        dir_names = path.split("/")
        for dir_name in dir_names:
            if dir_name == "..":
                if stack:
                    stack.pop()
                    
            elif dir_name in ("", "."):
                continue

            else:
                stack.append(dir_name)
                
        return "/" + "/".join(stack)

if __name__ == "__main__":
    s = Solution()
    print(s.simplifyPath("/a/../c"))