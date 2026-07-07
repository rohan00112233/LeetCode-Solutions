class Solution:
    def sumAndMultiply(self, n: int) -> int:

        ans = 0
        sum = 0
        n1 = []
        n = str(n)
        for i in range(len(n)):
            if n[i] != '0':
                n1.append(n[i])
        if not n1:
            return 0   
        digitsum = 0

        for digit in n1:
            digitsum += int(digit)
        
        x = "".join(n1)
        x = int(x)

        return x * digitsum

        

        