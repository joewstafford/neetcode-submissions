class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = []
        by_position = sorted(zip(position,speed), key=lambda t: t[0], reverse=True)

        for pos, spd in by_position:
            time = (target - pos)/spd
            if not fleets or time > fleets[-1]:
                fleets.append(time)
        return(len(fleets))

