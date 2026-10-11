class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        if len(s)!=len(t):
            return False
        for i in s:
            count[i]=1+ count.get(i,0)
        for i in t:
            count[i]=count.get(i,0)-1
        for val in count.values():
            if val !=0:
                return False
        return True