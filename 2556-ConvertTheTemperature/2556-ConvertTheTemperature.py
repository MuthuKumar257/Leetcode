# Last updated: 8/11/2026, 6:35:15 PM
class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        a=[]
        k=celsius+273.15
        f=celsius*1.80+32.00
        return [k,f]