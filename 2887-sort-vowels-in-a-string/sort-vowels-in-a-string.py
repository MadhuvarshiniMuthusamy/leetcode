class Solution:
    def sortVowels(self, s: str) -> str:
        vowels=set("AEIOUaeiou")
        vow_char=[]
        for ch in s:
            if ch in vowels:
                vow_char.append(ch)
        vow_char.sort()
        result=[]
        vow_ind=0
        for ch in s:
            if ch in vowels:
                result.append(vow_char[vow_ind])
                vow_ind+=1
            else:
                result.append(ch)
        #return result
        return "".join(result)