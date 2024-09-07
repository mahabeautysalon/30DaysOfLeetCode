class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l = len(s1)
        m = len(s2)
        n = len(s3)

        memory = {}

        if l + m != n:
            return False

        def dsf(i,j,k):
            if i == l and j == m and k == n:
                return True

            if (i,j,k) in memory:
                return memory[(i,j,k)]
            if i < l and s1[i] == s3[k]:
                if dsf(i+1,j,k+1):
                    memory[(i,j,k)] = True
                    return True

            if j < m and s2[j] == s3[k]:
                if dsf(i, j+1, k+1):
                    memory[(i,j,k)] = True
                    return True
            
            memory[(i, j, k)] = False
            return False

        return dsf(0, 0, 0)
