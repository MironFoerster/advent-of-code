import re
import math

test = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

val = [35, 46]  # validation value for example, paste from puzzle page, len determines if part 1/2

match len(val):
    case 1:
        def solution(d):
            lns = [[ln.split(" ") for ln in blc.split("\n")] for blc in d.split("\n\n")]
            print(lns)
            seeds = [int(s) for s in lns[0][0][1:]]

            maps = [[[int(i) for i in ln] for ln in blc[1:]] for blc in lns[1:]]
            print(maps)
            
            locs = []

            for seed in seeds:
                val = seed
                print(val)
                for map in maps:
                    print("map")
                    print(map)
                    for ln in map:
                        if ln[1] <= val < ln[1]+ln[2]:
                            print(ln)
                            val += ln[0] - ln[1]
                            print(val)
                            break
                    print(val)
                locs.append(val)
    
            answer = min(locs)
            return answer
    case 2:
        def solution(d):
            # previous approach too slow, so for second puzzle traversing the maps in reverse
            lns = [[ln.split(" ") for ln in blc.split("\n")] for blc in d.split("\n\n")]
            print(lns)
            sds = [int(s) for s in lns[0][0][1:]]

            maps = [[[int(i) for i in ln] for ln in blc[1:]] for blc in lns[1:]]

            for map in maps:
                for ln in map:
                    ln.append(ln[2] + ln[0])
                    ln.append(ln[0] - ln[1])

            loc = 0          
            while True:
                val = loc

                for map in reversed(maps):
                    for ln in map:
                        if ln[0] <= val < ln[3]:
                            val -= ln[4]
                            break

                
                for i, r in zip(sds[::2], sds[1::2]):
                    if i <= val < i+r:
                        return loc
                loc+=1