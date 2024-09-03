def countVowels(s):
    count = 0
    for ch in s:
        if ch in "aeiou":
            count+=1
    return count

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        V = countVowels(s[:k])
        maxVowel = V
        vowel = "aeiou"
        for i in range(1,n-k+1):
            if s[i-1] in vowel and s[i+k-1] not in vowel:
                V -=1
            elif s[i-1] not in vowel and s[i+k-1] in vowel:
                V +=1
            #print(f"Value of V : {V}")
            if maxVowel < V:
                maxVowel +=1
            #print(f"Max Vowel : {maxVowel}")
        return maxVowel
                