import re

test = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

val = [13, 30]  # validation value for example, paste from puzzle page, len determines if part 1/2

match len(val):
    case 1:
        def solution(d):
            lns = [[list(filter(None, side.split(" "))) for side in ln.replace(":", "|").split("|")[1:]] for ln in d.split("\n")]
            print(lns)
            
            for ln in lns:
                ln[1] = list(map(lambda x: 1 if x in ln[0] else 0, ln[1]))
            print(lns)
            matches = [sum(ln[1]) for ln in lns]
            
    
            answer = sum(2**(n-1) if n>0 else 0 for n in matches)
            return answer
    case 2:
        def solution(d):
            lns = [[list(filter(None, side.split(" "))) for side in ln.replace(":", "|").split("|")[1:]] for ln in d.split("\n")]
            answer = len(lns)
            active_lns = range(answer)
            while active_lns:
                print(len(active_lns))
                print(active_lns[:10])
                new_active = []
                for i in active_lns:
                    new_active.extend([i+1+j for j in range(sum(list(map(lambda x: 1 if x in lns[i][0] else 0, lns[i][1]))))])
                active_lns = new_active.copy()

                answer += len(active_lns)
            
            return answer