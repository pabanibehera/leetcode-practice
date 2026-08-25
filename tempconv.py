class Solution:
    def convertTemperature(self, celsius: float,) -> List[float]:
        Kelvin=273.15 + celsius
        Fahrenhit=(celsius*1.80)+32.00
        ans=[Kelvin,Fahrenhit]
        return ans        