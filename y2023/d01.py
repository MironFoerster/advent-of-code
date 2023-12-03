import re

test = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

val = [142, 281]  # len determines if part 1/2

match len(val):
    case 1:
        def solution(d):
            lns = [int(re.findall("\d", ln)[0] + re.findall("\d", ln)[-1]) for ln in d.split("\n")]    
    
            a = sum(ln for ln in lns)
            return a
    case 2:
        def solution(d):

            str2num = {
                "one": "o1e",
                "two": "t2o",
                "three": "t3e",
                "four": "f4r",
                "five": "f5e",
                "six": "s6x",
                "seven": "s7n",
                "eight": "e8t",
                "nine": "n9e",
            }

            def replace_words(text):
                for k, v in str2num.items():
                    text = text.replace(k, v)
                return text

            fake = [int(l[0] + l[-1]) for l in re.sub(r"[A-z]", "", replace_words(d)).split("\n")]


            nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

            def mp(num):
                try:
                    int(num)
                    return num
                except:
                    return str(nums.index(num))
                
            lns = [int(mp(re.findall("\d|"+"|".join(nums), ln)[0]) + mp(list(re.finditer("\d|"+"|".join(nums), ln))[-1].group())) for ln in d.split("\n")]    
            
            print(len(d.split("\n")))
            for i in list(zip(d.split("\n"), lns, fake)):
                if i[1] != i[2]:
                    print(i)
            print(len(lns))

            a = sum(ln for ln in lns)
            return a