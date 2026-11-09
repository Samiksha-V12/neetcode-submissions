class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        di = {}

        for i in strs:
            a = sorted(i)
            b = "".join(a)

            if b in di:
                di[b].append(i)
            else:    
                di.update({b:[i]})
        
        return list(di.values())