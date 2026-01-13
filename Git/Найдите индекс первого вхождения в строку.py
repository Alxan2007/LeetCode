class Solution(object):
    def strStr(self, haystack, needle):
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle: # Берет срез строки haystack
                # i: - начальный позиция   i + len(needle) - конечная позиция и сравниваем полученный код с искомой строкой
                return i
            if needle == "":
                return 0
        return -1