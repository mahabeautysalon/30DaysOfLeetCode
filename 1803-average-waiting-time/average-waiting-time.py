class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        finish = 0
        if len(customers)>0:
            finish=customers[0][0]
        waiting = []
        for row in customers:
            if finish<row[0]:
                finish = row[0]+row[1]
                waiting.append(row[1])
            else:
                finish += row[1]
                waiting.append(finish-row[0])
            #print(waiting)
        average = ((sum(waiting))/len(waiting))
        return average