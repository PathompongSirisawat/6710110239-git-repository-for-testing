def alternate(s):
    unique_chars = list(set(s))
    max_length = 0
    
    for i in range(len(unique_chars)):
        for j in range(i + 1, len(unique_chars)):
            char1, char2 = unique_chars[i], unique_chars[j]
            filtered = [c for c in s if c in (char1, char2)]
            
            if all(filtered[k] != filtered[k+1] for k in range(len(filtered) - 1)):
                max_length = max(max_length, len(filtered))
    
    return max_length

if __name__ == "__main__":
    n = int(input().strip())
    s = input().strip()
    print(alternate(s))