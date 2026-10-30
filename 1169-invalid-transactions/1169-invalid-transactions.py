class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        parsed = []

        for transaction in transactions:
            name, time, amount, city = transaction.split(",")
            parsed.append((name, int(time), int(amount), city))
        
        invalid = set()
        n = len(transactions)

        for i in range(n):
            name1, time1, amount1, city1 = parsed[i]

            if amount1 > 1000:
                invalid.add(i)
            for j in range(i + 1, n):
                name2, time2, amount2, city2 = parsed[j]

                if(name1 == name2 and city1 != city2 and abs(time1 - time2) <= 60):
                    invalid.add(i)
                    invalid.add(j)
        return [transactions[i] for i in range(n) if i in invalid]
        