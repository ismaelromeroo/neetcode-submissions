class Solution:
    def isPalindrome(self, s: str) -> bool:
        n,m=0 , len(s) - 1
        while (n < m):
            while( n<m and not s[n].isalnum()):
                n+=1
            while( m>n and not s[m].isalnum()):
                m-=1
            if(s[n].lower() != s[m].lower()):
                return False
            n+=1
            m-=1
        return True
        