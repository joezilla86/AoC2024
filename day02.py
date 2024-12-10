
def safe(report: list[int]) -> bool:
    diffs = []
    for i, val in enumerate(report[:-1]):
        diffs.append(report[i+1] - val)

    abs_diffs = [abs(x) for x in diffs]
    if (max(abs_diffs) <= 3) and (min(abs_diffs) > 0) and (max(diffs) * min(diffs) > 0):
        return True
    else:
        return False

def permute(report):
    for i in range(len(report)):
        temp1 = report[:i]
        temp2 = report[i+1:]
        temp1.extend(temp2)
        if safe(temp1):
            return True
    return False

def main():
    with open("C:/Users/janderson/Repos/AoC2024/day02.txt", "r") as f:
        raw = f.readlines()
    data = parse(raw)

    result1 = 0
    result2 = 0
    for report in data:
        if safe(report):
            result1 += 1
        elif permute(report):
            result2 += 1
    
    print(f"Part 1: {result1}")
    print(f"Part 2: {result1+result2}")
        

def parse(raw):
    result = []
    for line in raw:
        result.append([int(x) for x in line.split(" ")])
    return result

main()