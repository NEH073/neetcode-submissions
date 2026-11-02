class Solution:

    def encode(self, strs: List[str]) -> str:
        enc=""
        for s in strs:
            enc += str(len(s))+"#"+s
        return enc

    def decode(self, s: str) -> List[str]:
            i=0
            res=[]
            while i<len(s):
                start=i
                while s[i]!="#":
                    i+=1
                length = int(s[start:i])
                i+=1
                res.append(s[i:i+length])
                i+=length
            return res