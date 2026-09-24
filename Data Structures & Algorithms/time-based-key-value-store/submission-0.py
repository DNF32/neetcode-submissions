class TimeMap:

    def __init__(self):
        self.table = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.table:
            self.table[key].append((timestamp,value))
        else:
            self.table[key] = [(timestamp,value)]
    def get(self, key: str, timestamp: int) -> str:
        if key in self.table:
            values = self.table[key]
            left = 0 
            right = len(values) - 1

            maxTime = 0
            maxTimeIx = -1
            while left<= right:
                mid = (left + right) // 2

                midTime, midValue = values[mid]

                if midTime<= timestamp:
                    left = mid + 1
                    if midTime > maxTime:
                        maxTime =  midTime
                        maxTimeIx = mid
                else:
                    right = mid -1
            return "" if maxTimeIx == -1 else values[maxTimeIx][1]
        else:
            return ""

        
