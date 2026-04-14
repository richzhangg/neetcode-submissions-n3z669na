class Solution:
    def calPoints(self, operations: List[str]) -> int:
        lists = []
        for i in operations:
            if i == '+':
                lists.append(lists[-1]+lists[-2])
            elif i == 'C':
                lists.pop()
            elif i == 'D':
                lists.append(lists[-1]*2)
            else:
                lists.append(int(i))
        return sum(lists)