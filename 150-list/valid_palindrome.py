import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0: return False
        s = re.sub('[^a-zA-Z0-9]+', '', s).lower()
        i = 0
        j = len(s) - 1
        while True:
            if i == j or i==len(s):
                break
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

if __name__ == '__main__':
    input_var = "A man, a plan, a canal: Panama"
    outp = Solution().isPalindrome(input_var)
    print(outp)