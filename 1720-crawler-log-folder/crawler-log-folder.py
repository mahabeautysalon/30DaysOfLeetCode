class Solution:
    def minOperations(self, logs: List[str]) -> int:
        logsList = []
        for val in logs:
            if val[-2] == '.':
                if len(val) > 2:
                    if len(logsList) > 0:
                        logsList.pop()
            else:
                logsList.append(val)
        return len(logsList)