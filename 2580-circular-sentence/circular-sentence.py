class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sen = sentence.split()
        #print(sen)
        if(sentence[0] == sentence[-1]):
            for i in range(len(sen)-1):
                if(sen[i][-1] != sen[i+1][0]):
                    return False
        else:
            return False
        return True