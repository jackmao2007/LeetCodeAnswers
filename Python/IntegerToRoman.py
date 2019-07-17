class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        final = ''
        hc = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
        div = 1000
        for i in range(0, 8, 2):
            digit = num // div
            num = num % div
            if digit == 9:
                final += hc[i] + hc[i-2]
            elif digit == 4:
                final += hc[i] + hc[i-1]
            else:
                final += (digit // 5) * hc[i-1] + (digit % 5) * hc[i]
            div = div // 10
        return final


if __name__ == "__main__":
    s = Solution()
    num = 9
    s.intToRoman(9)

