class Solution(object):
    def myAtoi(self, st):
        """
        :type str: str
        :rtype: int
        """

        s = st.strip(' ')
        if s and not s[0].isnumeric() and s[0] != '-':
            return 0
        i = 1
        while i < len(s) and s[i].isnumeric():
            i += 1
        print(s[:i])
        return int(s[:i])

if __name__ == "__main__":
    s = Solution()
    num = '42'
    s.myAtoi(num)
