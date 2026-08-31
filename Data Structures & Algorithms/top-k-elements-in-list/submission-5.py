class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        #Creates buckets for every single number
        freq = [[] for i in range(len(nums) + 1)]
        
        #counts frequency of each nums occurence
        for num in nums:
            count[num] = 1 + count.get(num,0)
        #puts occurences into buckets of how many times they occur
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        #empty list for output
        res=[]
        #works back from most to least frequent numbers
        for i in range(len(freq) - 1,0, -1):
            #each occurence in bucket
            for num in freq[i]:
                #adds till required added
                res.append(num)
                if len(res) == k:
                    return res

                