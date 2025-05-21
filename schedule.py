class Solution:
    def generateSchedule(self, info) -> str:
        TIMEZONE_SHIFT = 5
        WEEK_SEQUENCE = [5,6,7,1,2,3,4]
        WEEK = {
            1: "Mon",
            2: "Tue",
            3: "Wed",
            4: "Thu",
            5: "Fri",
            6: "Sat",
            7: "Sun",
        }
        days = defaultdict(list)
        
        def getHour(h: int, isEnd = False):
            hour = h + TIMEZONE_SHIFT
            if isEnd and hour > 24:
                hour = hour % 24
                return hour, 1
            if not isEnd and hour >= 24:
                hour = hour % 24
                return hour, 1
            if isEnd and hour <= 0:
                hour = 24 - hour
                return hour, -1
            if not isEnd and hour < 0:
                hour = 24 - hour
                return hour, -1
            return hour, 0

        def generateHoursForTheDay(day: int, startHour: int, endHour: int, exceptionHours: Set[int]) -> None:
            currPeriodStart = startHour
            for h in range(startHour, endHour + 1):
                if h in exceptionHours or h == endHour:
                    if currPeriodStart != h:
                        start, startDayShift = getHour(currPeriodStart)
                        end, endDayShift = getHour(h, True)
                        if endDayShift != startDayShift:
                            days[day + startDayShift].append((start, 24))
                            days[day + endDayShift].append((0, end))
                        else:
                            days[day + endDayShift].append((start, end))
                    currPeriodStart = h + 1

        for day, dayInfo in info.items():
            exceptions, start, end = dayInfo
            generateHoursForTheDay(day, start, end, exceptions)
        
        ans = []
        for day in WEEK_SEQUENCE:
            if day not in days:
                ans.append(f"{WEEK[day]}: -;")
            else:
                hours = ", ".join([f"{start}-{end}" for start, end in days[day]])
                ans.append(f"{WEEK[day]}: {hours};")
        return " ".join(ans)

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        print(self.generateSchedule({
            5: ({14,15}, 7, 17),
            6: ({}, 6, 9),
            1: ({18}, 7, 20),
            3: ({18}, 7, 20),
            4: ({13,18}, 7, 20),
        }))
        
