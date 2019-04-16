def parenthesis(left, right):
    if left == 1:
        yield '(' + ')' * right
    else:
        for i in range(right-left+2):
            for s in parenthesis(left-1, right-i):
                yield '('+ ')'*i +s

def generateParenthesis(n):
    return list(parenthesis(n,n))
