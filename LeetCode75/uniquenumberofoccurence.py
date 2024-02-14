class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = collections.Counter(arr)
        print(c)
        print(set(c.values()))
        return len(c) == len(set(c.values())) 
