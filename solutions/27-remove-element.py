from inplace import list_inplace_remove

def removeElement(A, elem):
    return list_inplace_remove(A, lambda x: x == elem)
