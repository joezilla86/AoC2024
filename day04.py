
def main():
    with open("C:/Users/janderson/Repos/AoC2024/day04.txt", "r") as f:
        raw = f.read().splitlines()

    data = parse(raw)
    #data = raw
    print(data)
    
    xs = find_c(data, "X")
    a_s = find_c(data, "A")
    
    result1 = 0
    for loc in xs:
        result1 += find_xmas(data, loc)
    
    result2 = 0
    for loc in a_s:
        result2 += find_x_mas(data, loc)

    print(f"Part 1: {result1}")
    print(f"Part 2: {result2}")


def parse(raw):
    width = len(raw[0]) + 6
    height = len(raw) + 6

    # Create blank grid of input with 3 cells of buffer around full perimeter
    # this will remove the need to perform boundary checks
    grid = []
    for y in range(height):
        if y < 3 or y > height - 3:
            grid.append(["."] * width)
        else:
            grid.append([])
            for x in range(width):
                if 3 <= x <= (width - 3):
                    try:
                        grid[y].append(raw[y-3][x-3])
                    except IndexError:
                        grid[y].append(".")
                else:
                    grid[y].append(".")
                    


    #[[raw[y-3][x-3] if (3<=y<=(height-3) and 3<=x<=(width-3)) else "." for x in range(width) ] for y in range(height)]

    return grid

def find_c(data, c):
    result = set()
    for y, row in enumerate(data):
        for x, char in enumerate(row):
            if char == c:
                result.add((x,y))
    return result

def find_xmas(data, loc: tuple):
    # (x, y) is the location within data of the X character
    # XMAS can appear in any direction eminating from the X
    # Directions are numbered in the diagram below
    #
    #    123
    #    4X5
    #    678
    x, y = loc
    result = 0
    # Direction 1
    if data[y-1][x-1] == "M" and data[y-2][x-2] == "A" and data[y-3][x-3] == "S":
        result += 1
    # Direction 2
    if data[y-1][x] == "M" and data[y-2][x] == "A" and data[y-3][x] == "S":
        result += 1
    # Direction 3
    if data[y-1][x+1] == "M" and data[y-2][x+2] == "A" and data[y-3][x+3] == "S":
        result += 1
    # Direction 4
    if data[y][x-1] == "M" and data[y][x-2] == "A" and data[y][x-3] == "S":
        result += 1
    # Direction 5
    if data[y][x+1] == "M" and data[y][x+2] == "A" and data[y][x+3] == "S":
        result += 1
    # Direction 6
    if data[y+1][x-1] == "M" and data[y+2][x-2] == "A" and data[y+3][x-3] == "S":
        result += 1
    # Direction 7
    if data[y+1][x] == "M" and data[y+2][x] == "A" and data[y+3][x] == "S":
        result += 1
    # Direction 8
    if data[y+1][x+1] == "M" and data[y+2][x+2] == "A" and data[y+3][x+3] == "S":
        result += 1
    return result

def find_x_mas(data, loc):
    x, y = loc
    result = 0
    # loc is (x,y) tuple of location of the "A" character
    # X-MAS 
    if (data[y-1][x-1] == "M" and data[y+1][x+1] == "S") or (data[y+1][x+1] == "M" and data[y-1][x-1] == "S"):
        if (data[y+1][x-1] == "M" and data[y-1][x+1] == "S") or (data[y-1][x+1] == "M" and data[y+1][x-1] == "S"):
            result += 1
    
    elif (data[y][x-1] == "M" and data[y][x+1] == "S") or (data[y][x+1] == "M" and data[y][x-1] == "S"):
        if (data[y-1][x] == "M" and data[y+1][x] == "S") or (data[y+1][x] == "M" and data[y-1][x] == "S"):
            result += 1
    
    return result

main()