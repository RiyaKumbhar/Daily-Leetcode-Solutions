class Solution:
    def getFolderNames(self, names: list[str]) -> list[str]:
        used = {}
        result = []

        for name in names:
            if name not in used:
                result.append(name)
                used[name] = 1

            else:
                k = used[name]

                while f"{name}({k})" in used:
                    k += 1
                
                new_name = f"{name}({k})"
                result.append(new_name)

                used[new_name] = 1
                used[name] = k + 1
        return result
        