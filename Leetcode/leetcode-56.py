# Merge Intervals
# Given a collection of intervals,merge all overlapping intervals

class Solution:

    def merge(self, intervals: list[list[int]]):
        if not intervals:
            return intervals
        intervals.sort(key=lambda x:x[0])
        result = []
        for interval in intervals:
            if result == [] or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1])
        return result


if __name__ == "__main__":
    intervals = [[1,3], [2,6], [8,10], [15,18]]
    s = Solution()
    print(s.merge(intervals))




