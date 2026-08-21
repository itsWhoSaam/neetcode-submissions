from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        stu_q = deque(students)
        san_stk = sandwiches
        san_stk.reverse()
        attempts = 0
        while attempts < len(stu_q):
            if (stu_q[0] == san_stk[-1]):
                stu_q.popleft()
                san_stk.pop()
                attempts = 0
            elif (stu_q[0] != san_stk[-1]):
                stu = stu_q.popleft()
                stu_q.append(stu)
                attempts += 1
        return len(stu_q)
