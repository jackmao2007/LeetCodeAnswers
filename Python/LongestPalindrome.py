class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == '':
            return ''
        sub = ''
        m = 0
        i = 0
        while i < len(s) * 2 - 1:
            mid = i // 2
            off = i % 2
            length = 0
            if s[mid] == s[mid+off]:
                length = 1 + off
                j = 1
                while mid - j >= 0 and mid + j < len(s) and s[mid-j] == s[mid+off+j]:
                    length += 2
                    j += 1
            if length > m:
                m = length
                sub = s[mid-j+1: mid+off+j]
            i += 1
        return sub


if __name__ == "__main__":
    s = Solution()
    s.longestPalindrome('ccc')

