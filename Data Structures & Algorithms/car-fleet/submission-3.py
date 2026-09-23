class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        count = 0
        lead_time = 0

        for pos, spd in sorted(zip(position,speed), key=lambda t: t[0], reverse=True):
            time = (target - pos)/spd
            if time > lead_time:
                count += 1
                lead_time = time
        return count

