from functools import reduce
import re

test = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

val = [8, 2286]  # validation value for example, paste from puzzle page, len determines if part 1/2

match len(val):
    case 1:
        def solution(d):
            colors = {
                "red": 12,
                "blue": 14,
                "green": 13
            }

            lns = [int(re.findall("\s(\d+):", ln)[0]) if all([int(re.findall("\s(\d+)\s", color)[0]) <= colors[re.findall("\s([A-Za-z]+)", color)[0]] for draw in ln.split(";") for color in draw.split(",")]) else 0 for ln in d.split("\n")]
    
            answer = sum(ln for ln in lns)
            return answer
    case 2:
        def solution(d):
            lns = [reduce(lambda x, y: x*y, [max(map(lambda x: int(x), re.findall("\s(\d+)\sred", ln))), max(map(lambda x: int(x), re.findall("\s(\d+)\sgreen", ln))), max(map(lambda x: int(x), re.findall("\s(\d+)\sblue", ln)))]) for ln in d.split("\n")]
    
            answer = sum(ln for ln in lns)
            return answer