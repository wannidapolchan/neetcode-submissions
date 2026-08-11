# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        pairs = list(pairs)
        result = [list(pairs)]

        if not pairs:
            return []
        for i in range(1, len(pairs)):
            curr = pairs[i]
            next = i - 1

            while next >= 0 and pairs[next].key > curr.key:
                pairs[next+1] = pairs[next]
                next -= 1
            
            pairs[next +1] = curr
            result.append(list(pairs))
        return result
