"""
>>> largestRectangleArea([2,1,5,6,2,3])
10
"""


def largestRectangleArea(height):
    largest = 0
    stack = []

    for i in range(len(height)):
        h = height[i]
        s = i

        while stack and h < stack[-1][0]:
            l, s = stack.pop()
            area = l * (i - s)
            if largest is None or area > largest:
                largest = area

        stack.append((h, s))

    i = len(height)

    while stack:
        l, s = stack.pop()
        area = l * (i - s)
        if largest is None or area > largest:
            largest = area

    return largest
