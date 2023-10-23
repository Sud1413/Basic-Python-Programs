# Simplified Fractions

class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        a = []
        for i in range(1,n):
            for j in range(i+1,n+1):
                if math.gcd(i, j) == 1:
                    a.append(str(i)+"/"+str(j))
        return a
