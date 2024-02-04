class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitute = [0]*(len(gain)+1)
        altitude_gain = 0
        for i in range(len(gain)+1):
            altitute[i] = altitude_gain
            if i < len(gain):
                altitude_gain += gain[i]
        return max(altitute)    