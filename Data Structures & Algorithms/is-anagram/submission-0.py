class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x = [0] * 27

        if (len(s) == len(t)):
            for ch in s:
                ascii_val = ord(ch)
                index = ascii_val - 97
                x[index] += 1
            for ch in t:
                ascii_val = ord(ch)
                index = ascii_val - 97
                if(x[index]>0):
                    x[index] -= 1
                else:
                    return False
            return True
        return False