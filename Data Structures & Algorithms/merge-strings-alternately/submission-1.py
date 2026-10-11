class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        for i in range(min(len(word1), len(word2))):
            ans += word1[i]
            ans += word2[i]
        
        longer_word = word1 if len(word1) >= len(word2) else word2
        shorter_word = word1 if len(word1) <= len(word2) else word2

        if len(word1) == len(word2):
            return ans
        
        for i in range(len(shorter_word), len(longer_word)):
            ans += longer_word[i]
        return ans
