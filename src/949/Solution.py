class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        count = Counter(arr)
        hours = 23
        minutes = 59
        
        
        def getMaxMinutesFromDigits(counter):
            for minute in range(minutes, -1, -1):
                minutes_can_be_formed = True
                minutes_counter = Counter(counter)
                minute_str = f"0{minute}" if minute < 10 else str(minute)
                for ch in minute_str:
                    digit = int(ch)
                    if digit not in minutes_counter or minutes_counter[digit] < 1:
                        minutes_can_be_formed = False
                        break
                    minutes_counter[digit] -= 1
                if minutes_can_be_formed:
                    return (True, minute_str)
            return (False, "")
        
        
        for hour in range(hours, -1, -1):
            hour_can_be_formed = True
            hour_counter = Counter(count)
            hour_str = f"0{hour}" if hour < 10 else str(hour)
            for ch in hour_str:
                digit = int(ch)
                if digit not in hour_counter or hour_counter[digit] < 1:
                    hour_can_be_formed = False
                    break
                hour_counter[digit] -= 1
            if hour_can_be_formed:
                can_be_formed, minute_str = getMaxMinutesFromDigits(hour_counter)
                if can_be_formed:
                    return f"{hour_str}:{minute_str}"
        
        return ""
            
        