class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Step 1: handle negative n (do this once, before the loop)
        if n < 0:
            x = 1/x
            n = abs(n)

        result = 1

        # Step 2: loop until n is used up
        while n > 0:
            # if n is odd, set aside one copy of x
            if n % 2 !=0 :
                result = x * result 

            # square x, halve n
            x = x * x
            n = n //2

        return result