class Solution:
    # 투 포인터 함수
    def lrchecker(self, left: int, right: int, s:str) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    def longestPalindrome(self, s: str) -> str:
        answer = s[0]
        if len(s) == 1:
            return answer
        for i in range(1,len(s)):
            if s[i-1] == s[i]:
                cur_palindrome = self.lrchecker(i-1,i,s)
                if len(answer) < len(cur_palindrome):
                    answer = cur_palindrome
            if i < len(s)-1:
                if s[i-1] == s[i+1]:
                    cur_palindrome = self.lrchecker(i-1,i+1,s)
                    if len(answer) < len(cur_palindrome):
                        answer = cur_palindrome
        return answer