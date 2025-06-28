class Solution(object):
    def strStr(self, haystack, needle):
        n, m = len(haystack), len(needle)
        if m == 0:
            return 0  # empty needle always matches at index 0
        for i in range(0, n - m + 1):
            if haystack[i : i + m] == needle:
                return i
        return -1
        