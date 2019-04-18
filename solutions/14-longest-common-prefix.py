from iterator import izip, takewhile, imap

def longestCommonPrefix(strs):
    return "".join(c[0] for c in takewhile(lambda x: len(set(x))==1, izip(*strs)))
