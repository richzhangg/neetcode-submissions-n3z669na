class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        length = len(students)
        counter = Counter(students)
        for i in sandwiches:
            if counter[i] > 0:
                length -= 1
                counter[i] -= 1
            else:
                return length
        return length