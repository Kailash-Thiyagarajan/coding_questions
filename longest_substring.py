
"""
Given a string s, find the length of the longest substring without repeating characters.

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3
"""


def lengthOfLongestSubstring(s: str) -> int:
        
    d = {}
    max_len = 0
    
    left = 0
    
    for idx, ch in enumerate(s):
        if ch in d and d[ch] >= left:
            left = d[ch] + 1
        else:
            max_len = max(max_len, idx - left + 1)
        d[ch] = idx
    
    return max_len
