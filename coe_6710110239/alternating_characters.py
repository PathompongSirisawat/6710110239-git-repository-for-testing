def alternating_characters(s: str) -> int:
    if not s:  
        return 0
    
    deletions = sum(1 for i in range(1, len(s)) if s[i] == s[i - 1])
    return deletions

def main() -> None:
    try:
        q = int(input().strip())
        results = [alternating_characters(input().strip()) for _ in range(q)]
        for result in results:
            print(result)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == '__main__':
    main()
