"""
>>> lengthOfLongestSubstring("abcabcbb")
3
>>> lengthOfLongestSubstring("bbb")
1
"""

def lengthOfLongestSubstring(s):
    longest = 0
    current = 0
    last = {}

    for i,c in enumerate(s):
        l = last.get(c, None)
        last[c] = i
        if l is None:
            current += 1
        else:
            longest = max(current, longest)
            current = i - l
            last = { k:v
                     for (k,v) in last.items()
                     if v > l}

    return max(current, longest)
