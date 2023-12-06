import re, math
import functools as ft

test = """Time:      7  15   30
Distance:  9  40  200"""

val = [288, 71503]  # validation value for example, paste from puzzle page, len determines if part 1/2

match len(val):
    case 1:
        def solution(d):
            lns = [re.findall("\d+", ln) for ln in d.split("\n")]
            rcs = []

            for T, d in zip(lns[0], lns[1]):
                c = 0
                for t in range(1, int(T)):
                    if (int(T)-t) * t > int(d):
                        c +=1
                rcs.append(c)

            print(rcs)
            answer = ft.reduce(lambda x, y: x*y, rcs)
            return answer
    case 2:
        def solution(d):
            lns = ["".join(re.findall("\d+", ln)) for ln in d.split("\n")]
            c = 0
            for t in range(1, int(lns[0])):
                if (int(lns[0])-t) * t > int(lns[1]):
                    c +=1

            return c