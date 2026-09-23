class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = []
        pairs = list(zip(position,speed))
        by_position = sorted(pairs, key=lambda t: t[0], reverse=True)

        for pos, spd in by_position:
            time = (target - pos)/spd
            if not fleets or time > fleets[-1]:
                fleets.append(time)
        return(len(fleets))

