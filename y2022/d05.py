test = """"""

val = [,]  # len determines if part 1/2

match len(val):
    case 1:
        def s(d):
            import parse
            p = parse.compile("[{char}]")
            lns = [i for i in d.split("\n")]
            d = [[], [], []]
            for i in lns:
                d[0].append(p.parse(i[:3]))
                d[1].append(p.parse(i[4:7]))
                d[2].append(p.parse(i[8:]))

            for i in lns:
                for j in i:

    
            
    
            a = sum(ln for ln in lns)
            return a
    case 2:
        def s(d):
            pass
            