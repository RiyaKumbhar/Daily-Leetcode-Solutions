class Solution:
    def calculateTax(self, brackets: list[list[int]], income: int) -> float:
        total_tax = 0
        previous = 0

        for upper, percent in brackets:
            taxable = min(income, upper) - previous

            if taxable <= 0:
                break
            
            total_tax += taxable * percent / 100.0
            previous = upper
        return total_tax