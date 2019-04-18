from digit import digits2int_b
from binary_tree import iter_path

def sumNumbers(root):
    return sum(digits2int_b(path) for path in iter_path(root))

