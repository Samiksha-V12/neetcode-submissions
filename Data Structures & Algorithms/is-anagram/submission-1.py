class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      
        sna = {}
        tna = {}
        if(len(s) == len(t)):
                for ch in s:
                    if ch in sna:
                        sna[ch] +=1 
                    else:
                        sna.update({ch:1})

                for ch in t:
                    if ch in tna:
                        tna[ch] += 1
                    else:
                        tna.update({ch:1})

                if(sna == tna):
                    return True
        return False


