from combinatorics import product

def letterCombinations(digits):
    CHARS = {              "2": "abc", "3": "def",
              "4": "ghi",  "5": "jkl", "6": "mno",
              "7": "pqrs", "8": "tuv", "9": "wxyz"}

    return ["".join(a) for a in product(*[CHARS[d] for d in digits])]
