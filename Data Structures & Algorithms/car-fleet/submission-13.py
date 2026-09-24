class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        data = zip(position, speed)
        data =sorted(data,key= lambda x: x[0], reverse=True)
        fleets = []

        for pos,vel in data:
            time = (target- pos)/ vel
            if not fleets or time > fleets[-1]:
                fleets.append(time)
        return len(fleets)

