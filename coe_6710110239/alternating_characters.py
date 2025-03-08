def alternating_characters(s: str) -> int:
    deletions = 0
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            deletions += 1
    return deletions

if __name__ == '__main__':
    q = int(input())
    results = []
    for _ in range(q):
        s = input()
        result = alternating_characters(s)
        results.append(result)
    for result in results:
        print(result)