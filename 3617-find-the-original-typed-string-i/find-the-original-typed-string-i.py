class Solution:
    def possibleStringCount(self, word: str) -> int:
        n=len(word)
        total=1
        i=0
        while i<n:
            j=i
            while j<n and word[i]==word[j]:
                j+=1
            runlen=j-i
            total+=runlen-1
            i=j
        return total