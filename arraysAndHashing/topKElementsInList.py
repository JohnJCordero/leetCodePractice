from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = {}
        resultArray = []
        freqArray = [[] for i in range(len(nums) + 1)]

        for n in nums:
            countMap[n] = 1 + countMap.get(n, 0)

        for n, c in countMap.items():
            freqArray[c].append(n)


        for i in range(len(freqArray) - 1, 0, -1):
            for n in freqArray[i]:
                resultArray.append(n)
                if len(resultArray) == k:
                    return resultArray