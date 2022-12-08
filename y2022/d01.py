test = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

val = [24000,45000]  # len determines if part 1/2

match len(val):
    case 1:
        def s(d):
            mx = 0
            cur = 0
            rem = d + "\n\n"

            while rem != "":
                nxt = rem.find("\n")
                if rem.find("\n\n") == nxt:
                    cur += int(rem[:nxt])
                    if cur > mx:
                        print("A")
                        print(cur)
                        print(mx)
                        mx = cur
                    cur = 0
                    rem = rem[nxt+2:]
                else:
                    cur += int(rem[:nxt])
                    rem = rem[nxt+1:]
            a = mx
            return a

    case 2:
        def s(d):
            mx = [0,0,0]
            cur = 0
            rem = d + "\n\n"

            while rem != "":
                nxt = rem.find("\n")
                if rem.find("\n\n") == nxt:
                    cur += int(rem[:nxt])
                    if any([m<cur for m in mx]):
                        mx[0] = cur
                        mx.sort()
                    cur = 0
                    rem = rem[nxt+2:]
                else:
                    cur += int(rem[:nxt])
                    rem = rem[nxt+1:]

            a = sum(mx)
            return a