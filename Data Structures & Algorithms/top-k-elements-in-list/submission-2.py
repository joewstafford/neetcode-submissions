class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)
        top = []
        for number, count in frequency.most_common(k):
            top.append(number)
        return top
            

        