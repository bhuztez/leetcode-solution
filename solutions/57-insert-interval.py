from misc import merge_intervals

def insert(intervals, newInterval):
    intervals.append(newInterval)
    intervals.sort(key=lambda x:x.start)
    return list(merge_intervals(intervals))
