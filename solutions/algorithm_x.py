# http://www.cs.mcgill.ca/~aassaf9/python/algorithm_x.html

def select(Cols, Rows, r):
    cols = []

    for c in Rows[r]:
        for row in Cols[c]:
            for col in Rows[row]:
                if col != c:
                    Cols[col].remove(row)
        cols.append(Cols.pop(c))

    return cols


def deselect(Cols, Rows, r, cols):
    for c in Rows[r][::-1]:
        Cols[c] = cols.pop()
        for row in Cols[c]:
            for col in Rows[row]:
                if col != c:
                    Cols[col].add(row)


def solve(Cols, Rows, solution, is_primary=None):
    if is_primary:
        primaries = {
            k:v for k, v in Cols.iteritems()
            if is_primary(k)
        }
    else:
        primaries = Cols

    if not primaries:
        yield solution

    else:
        rows = min(primaries.itervalues(), key=len)
        for r in list(rows):
            solution.append(r)

            cols = select(Cols, Rows, r)

            for s in solve(Cols, Rows, solution, is_primary):
                yield s

            deselect(Cols, Rows, r, cols)
            solution.pop()
