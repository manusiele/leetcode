class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_set = set()   # to store characters in current window
        left = 0           # left pointer of window
        max_len = 0        # maximum length found

        for right in range(len(s)):
            # if duplicate character found, shrink window from left
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            # add current character to window
            char_set.add(s[right])

            # update max length
            max_len = max(max_len, right - left + 1)

        return max_len
