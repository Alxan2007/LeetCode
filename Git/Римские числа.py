class Solution(object):
    def romanToInt(self, s):
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        for i in range(len(s)):
            current = roman_dict[s[i]]
            if i + 1 < len(s) and roman_dict[s[i + 1]] > current:
                result -= current
            else:
                result += current
        return result


