class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_vowel = 0
        vowel_count = 0
        start = 0

        vowels=set("aeiou")

        for i in range(len(s)):
            # if s[i]=='a' or s[i]== 'e' or s[i]=='i' or s[i]=='o' or s[i]=='u':
            if s[i] in vowels:
                vowel_count += 1
            
            if (i-start+1==k):
                max_vowel = max(max_vowel,vowel_count)
                # if s[start]=='a' or s[start]== 'e' or s[start]=='i' or s[start]=='o' or s[start]=='u':
                if s[start] in vowels:
                    vowel_count -= 1
                start += 1
                
        return max_vowel

