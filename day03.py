import re

def main():
    with open("C:/Users/janderson/Repos/AoC2024/day03.txt", "r") as f:
        raw = f.readlines()

    data = parse(raw)
    
    enable = True
    result = 0
    for line in data:
        if enable and line[:3] == "mul":
            result += mul(line)
        if line[:3] == "don":
            enable = False
        if line[:3] == "do(":
            enable = True
        #print(f"{line=}, {enable=}, {result=}")
        #_ = input()
    #result = sum([mul(x) for x in data])
    return result

def parse(raw: list[str]):
    #pattern = re.compile("mul\((\d{1,3},\d{1,3})\)")
    pattern = re.compile(r"(mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))")
    result = []
    for line in raw:
        result.extend(pattern.findall(line))
    
    return result

def mul(input: str) -> int:
    x, y = input[4:-1].split(",")
    return int(x) * int(y)

print(main())