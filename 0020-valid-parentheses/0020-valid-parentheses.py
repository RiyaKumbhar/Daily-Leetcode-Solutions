class Solution:
    def isValid(self, s: str) -> bool:
        a = []
        f = True
        for v in s:
            if(len(a) != 0 and v == ')' and a[-1] == '('):
                a = a[:-1]
            elif(len(a) != 0 and v == '}' and a[-1] == '{'):
                a = a[:-1]
            elif(len(a) != 0 and v == ']' and a[-1] == '['):
                a = a[:-1]
            else:
                a.append(v)
        if(len(a) != 0):
            f = False
        return f

        