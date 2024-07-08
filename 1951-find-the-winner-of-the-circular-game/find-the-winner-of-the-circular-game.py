class Solution(object):
    def findTheWinner(self, n, k):
        friends = range(1,n+1)
        position=0
        while len(friends)>1:
            position=((position+(k-1))%len(friends))
            friends.pop(position)
            #print(friends)
        return friends[0]
        