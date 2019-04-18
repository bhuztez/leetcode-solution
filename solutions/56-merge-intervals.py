from misc import merge_intervals


def merge(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x:x.start)
    return list(merge_intervals(intervals))
