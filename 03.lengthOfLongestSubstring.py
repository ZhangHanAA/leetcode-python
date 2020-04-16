"""
给定一个字符串，找出其中不含有重复字符的最长字串的长度。
"""


def lengthOfLongestSubstring(s: str) -> int:
    if not s:
        return 0
    left = 0
    n = len(s)
    max_len = 0
    cur_len = 0
    lookup = set()
    for i in range(n):
        cur_len += 1
        while s[i] in lookup:
            lookup.remove(s[left])
            left += 1
            cur_len -= 1
        if cur_len > max_len:
            max_len = cur_len
        lookup.add(s[i])

    return max_len


def test(s):
    if not s:
        return 0
    windows = []
    max_len = 0
    cur_len = 0

    for i in range(len(s)):
        cur_len += 1
        while s[i] in windows:
            windows.pop(0)
            cur_len -= 1
        windows.append(s[i])
        max_len = max(max_len, cur_len)

    return max_len


if __name__ == '__main__':
    s = "abcabcbb"
    res = lengthOfLongestSubstring(s)
    res2 = test(s)
    print(res)
    print(res2)
