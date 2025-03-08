def caesarCipher (s,k):
    k = k % 26
    result = ""
    for i in s:
        if i.isalpha():
            if i.islower():
                result += chr((ord(i) + k - 97) % 26 + 97)
            else:
                result += chr((ord(i) + k - 65) % 26 + 65)
        else:
            result += i
    return result

if __name__ == '__main__':
    n = int(input().strip())
    s = input()
    k = int(input().strip())
    result = caesarCipher(s, k)
    print(result)