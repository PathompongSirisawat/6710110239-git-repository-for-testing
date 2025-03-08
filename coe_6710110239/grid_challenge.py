def gridChallenge(grid):
    grid = ["".join(sorted(row)) for row in grid]
    for i in range(len(grid[0])):
        for j in range(1, len(grid)):
            if grid[j][i] < grid[j-1][i]:
                return "NO"
    return "YES"

if __name__ == '__main__':
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        grid = [input() for _ in range(n)]
        result = gridChallenge(grid)
        results.append(result)
    for result in results:
        print(result)