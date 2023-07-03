def fizzbuzz(n):
    numbers = []
    for number in range(1, n + 1):
        if number % 15 == 0:
            numbers.append('FizzBuzz')
        elif number % 5 == 0:
            numbers.append('Buzz')
        elif number % 3 == 0:
            numbers.append('Fizz')
        else:
            numbers.append(number)
    return numbers
