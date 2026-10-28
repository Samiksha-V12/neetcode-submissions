class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       
        if(len(s)!=len(t)):
           return False
        sna = {}  
        for ch in s:
            if ch in sna:
                sna[ch] += 1
            else:
                sna.update({ch:1}) 
        for ch in t:
            if ch not in sna or sna[ch] == 0:
                return False
            else:
                sna[ch] -= 1
        return True        
        