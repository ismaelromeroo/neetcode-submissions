class Solution:
    def isPalindrome(self, s: str) -> bool:
        n,m = 0, len(s) - 1
        while(n<m):
            while (not s[n].isalnum() and n<m):
                n+=1
            while (not s[m].isalnum() and m>n):
                m-=1
            if (not (s[n].lower() == s[m].lower())):
                return False
            n,m = n+1,m-1
        return True