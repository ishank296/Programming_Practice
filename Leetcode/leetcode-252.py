# Given an array of meeting time intervals , determine if a person
# could attend all the meetings


class Solution:

    def canattendmeetings(self, intervals: list[list[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])
        last_end = -1
        for interval in intervals:
            if last_end == -1 or last_end <= interval[0]:
                last_end = interval[1]
            else:
                return False
        return True


if __name__ == "__main__":
    intervals1 = [[0,30],[5,10],[15,20]]
    intervals2 = [[7,10],[2,4]]
    s = Solution()
    print(s.canattendmeetings(intervals1))
    print(s.canattendmeetings(intervals2))
