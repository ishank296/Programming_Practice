# Boats to save people
# Given a boat that can take at most 2 people at a time
# and maximum limit of weight w, find min number of boats needed
# to carry people given with list of weights

class Solution:

    def numrescueboats(self, people:list[int],limit)-> int:
        people.sort()
        res = 0
        while len(people) > 1:
            if people[-1] + people[0] <= limit:
                people.pop(0)
                people.pop()
            else:
                people.pop()
            res += 1
        if len(people) == 1:
            res += 1
        return res


if __name__ == "__main__":
    s = Solution()
    people = [3,2,2,1]
    people_2 = [3,5,4,3]
    limit = 3
    limit_2 = 5
    print(s.numrescueboats(people,3))
    print(s.numrescueboats(people_2,limit_2))