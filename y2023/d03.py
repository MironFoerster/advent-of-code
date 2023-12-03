import re
from mytools import *

test = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

val = [4361, 467835]  # validation value for example, paste from puzzle page, len determines if part 1/2

match len(val):
    case 1:
        def solution(d):
            lns = [ln for ln in d.split("\n")]
            grid = Grid(lns)
            answer = 0

            matches = re.finditer("(\d+)", grid.flat)
            
            for m in matches:
                l = len(m.group())
                adj = ""
                x, y = grid.coord_from_flat_index(m.start())
                
                x, y, value = grid.move_u_from(x, y)
                adj += value
                
                for _ in range(l):
                    
                    x, y, value = grid.move_r_from(x, y)
                    adj += value
                for _ in range(2):
                    
                    x, y, value = grid.move_d_from(x, y)
                    adj += value
    
                for _ in range(l+1):
                    x, y, value = grid.move_l_from(x, y)
                    adj += value
    
                for _ in range(2):
                    x, y, value = grid.move_u_from(x, y)
                    adj += value
    
                print(adj)

                if any(not c.isdigit() and c != "." for c in adj):
                    answer += int(m.group())

            return answer
    case 2:
        def solution(d):
            lns = [ln for ln in d.split("\n")]
            grid = Grid(lns)
            gears = {}

            def check_gear(x, y, value, match):
                if value != "*":
                    return
                else:
                    if str(x)+"gear"+str(y) in gears.keys():
                        gears[str(x)+"gear"+str(y)].append(int(match.group()))
                    else:
                        gears[str(x)+"gear"+str(y)] = [int(match.group())]
                
            matches = re.finditer("(\d+)", grid.flat)
            
            for m in matches:
                l = len(m.group())
                x, y = grid.coord_from_flat_index(m.start())
                
                x, y, value = grid.move_u_from(x, y)
                check_gear(x, y, value, m)
                
                for _ in range(l):
                    x, y, value = grid.move_r_from(x, y)
                    check_gear(x, y, value, m)

                for _ in range(2):
                    x, y, value = grid.move_d_from(x, y)
                    check_gear(x, y, value, m)
    
                for _ in range(l+1):
                    x, y, value = grid.move_l_from(x, y)
                    check_gear(x, y, value, m)
    
                for _ in range(2):
                    x, y, value = grid.move_u_from(x, y)
                    check_gear(x, y, value, m)


            answer = 0
            for gear in gears.values():
                answer += gear[0]*gear[1] if len(gear) == 2 else 0

            return answer