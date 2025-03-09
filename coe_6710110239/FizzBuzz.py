def FizzBuzz(number):
    result = []
    for num in range(1, number + 1):
        answer = ""
        if num % 3 == 0:
            answer += "Fizz"
        if num % 5 == 0:
            answer += "Buzz"
        if not answer:
            answer = str(num)
        result.append(answer)
    return result