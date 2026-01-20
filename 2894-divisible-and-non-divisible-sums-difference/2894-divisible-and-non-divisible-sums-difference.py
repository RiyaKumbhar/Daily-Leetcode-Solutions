class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        k = n // m

        total = (n * (n + 1)) // 2
        num2 = (k * (k + 1) // 2) * m
        num1 = total - num2

        return num1 - num2
        