test = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

val = [157,70]  # len determines if part 1/2

match len(val):
    case 1:
        def s(d):
            import string
            lns = [[i[:int(len(i)/2)], i[int(len(i)/2):]] for i in d.split("\n")]
            c = string.ascii_lowercase + string.ascii_uppercase
            a=0
            for l in lns:
                p = 0
                for x in sorted(list(set(l[0]))+list(set(l[1]))):
                    if p == x:
                        a += c.index(x)+1
                    p = x
            return a
    case 2:
        def s(d):
            import string
            lns = [i for i in d.split("\n")]
            c = string.ascii_lowercase + string.ascii_uppercase
            a=0
            for i in range(0, len(lns), 3):
                
                p = 0
                pp = 0
                for x in "".join(sorted("".join(["".join(set(l)) for l in lns[i:i+3]]))):
                    if p == pp == x:
                        a += c.index(x)+1
                    pp = p
                    p = x
            return a
            