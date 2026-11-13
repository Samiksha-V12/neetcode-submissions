class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic.update({i:1})
        
        res=[]

        bucket = [[] for i in range(len(nums)+1)]
        for number,frequency in dic.items():
            bucket[frequency].append(number)

        for i in range(len(bucket)-1,-1,-1):
            for number in bucket[i]:
                res.append(number)
                if len(res) == k:
                    return res
            