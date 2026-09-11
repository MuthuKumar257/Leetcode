# Last updated: 9/11/2026, 9:29:28 AM
class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        a=[]
        k=celsius+273.15
        f=celsius*1.80+32.00
        return [k,f]