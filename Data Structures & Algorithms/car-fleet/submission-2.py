class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = []
        
        for pos, spd in sorted(zip(position,speed), key=lambda t: t[0], reverse=True):
            time = (target - pos)/spd
            if not fleets or time > fleets[-1]:
                fleets.append(time)
        return(len(fleets))

