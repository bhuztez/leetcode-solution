def combinationSum2(candidates, target):
    results = [[] for i in range(0, target+1)]
    results[0].append(())

    candidates.sort(reverse=True)

    for c in candidates:
        for i in range(target, c-1, -1):
            results[i].extend((c,)+r for r in results[i-c])

    return map(list, set(results[target]))
