class Solution(object):
    def passThePillow(self, n, time):
        forward=True
        people = 1
        while time >0:
            if forward:
                people+=1
                if people == n:
                    forward = False
            else:
                people-=1
                if people == 1:
                    forward = True
            time-=1
        return people
        