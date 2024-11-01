class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        sen = sentence.split()
        dictionary = sorted(dictionary,key=len)
        #print(sen)
        ans = []
        for i in range(len(sen)):
            check = True
            for word in dictionary:
                if(sen[i].find(word) == 0):
                    check = False
                    ans.append(word)
                    break
            if check:
                ans.append(sen[i])
            #print(ans)
        return " ".join(ans)
        