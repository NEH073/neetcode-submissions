class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      count = {}
      for num in nums:
        count[num]=count.get(num,0)+1  
      after_sorted=sorted(count,key=count.get,reverse=True)
      return (after_sorted[:k])