class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic = {'2': 'abc', '3': 'def',
               '4': 'ghi', '5': 'jkl',
               '6': 'mno', '7': 'pqrs',
               '8': 'tuv', '9': 'wxyz'}

        # base case:
        if digits == "":
            return []
        if len(digits) == 1:
            return list(dic[digits[0]])
        # recursive step:
        output = []
        for c in dic[digits[0]]:
            for tails in self.letterCombinations(digits[1:]):
                output.append(c + tails)
        return output
