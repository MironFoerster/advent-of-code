test = """A Y
B X
C Z"""

val = [15,12] # len determines if part 1/2

match len(val):
    case 1:
        def s(d):
            lns = [i.split(" ") for i in d.split("\n")]
    
            c = [3,0,6]
    
            a = sum("XYZ".index(ln[1])+1 + c[("ABC".index(ln[0])-"XYZ".index(ln[1]))%3] for ln in lns)
            return a
    case 2:
        def s(d):
            lns = [i.split(" ") for i in d.split("\n")]

            c = [0,3,6]
    
            a = sum(("ABC".index(ln[0])-"YXZ".index(ln[1]))%3+1 + c["XYZ".index(ln[1])] for ln in lns)
            return a
