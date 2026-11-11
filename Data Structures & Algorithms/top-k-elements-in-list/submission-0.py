class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic.update({i:1})

        res = []    

        sorted_dic = sorted(dic.items(),key = lambda x:x[1], reverse = True)
        for i in range (k):
            res.append(sorted_dic[i][0])
            
        return res
