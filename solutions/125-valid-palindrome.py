def isPalindrome(s):
    s = ''.join(c for c in s.lower() if c.isalnum())
    return s == s[::-1]
