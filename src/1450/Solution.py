from typing import List


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        students = 0
        for s,e in zip(startTime, endTime):
            if s <= queryTime <= e:
                students += 1
        return students
