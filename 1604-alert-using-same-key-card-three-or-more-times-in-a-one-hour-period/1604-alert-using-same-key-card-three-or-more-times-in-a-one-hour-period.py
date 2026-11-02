class Solution:
    def alertNames(self, keyName: list[str], keyTime: list[str]) -> list[str]:
        times = defaultdict(list)

        for name, time in zip(keyName, keyTime):
            hour, minute = map(int, time.split(":"))
            total_minutes = hour * 60 + minute
            times[name].append(total_minutes)

        result = []

        for name, entries in times.items():
            entries.sort()

            for i in range(2, len(entries)):
                if entries[i] - entries[i - 2] <= 60:
                    result.append(name)
                    break
        
        return sorted(result)
        