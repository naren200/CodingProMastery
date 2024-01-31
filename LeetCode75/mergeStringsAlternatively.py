class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        results = ""
        
        it = 0
        for e in word1:
            results = results + e
            if(len(word2)>=it+1):
                results = results + word2[it]
            print(it+1, len(word1))
            if(len(word1)<len(word2)) and it+1 == len(word1):
                for j in range(it+1, len(word2)):
                    results = results + word2[j]
            it = it + 1
            print(e)
        return results
        