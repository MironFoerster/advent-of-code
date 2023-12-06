import re, math
import functools as ft

test = """"""

val = []  # validation value for example, paste from puzzle page, len determines if part 1/2

match len(val):
    case 1:
        def solution(d):
            lns = [ln.split(" ") for ln in d.split("\n")]
    
            
    
            answer = sum(ln for ln in lns)
            return answer
    case 2:
        def solution(d):
            pass