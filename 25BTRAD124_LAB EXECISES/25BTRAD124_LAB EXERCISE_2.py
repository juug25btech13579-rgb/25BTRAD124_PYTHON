# ---------------------------------------------------------------------------
# Lab Exercise 5: Number guessing game
# ---------------------------------------------------------------------------
def lab5_guessing_game():
    number = random.randint(1, 100)
    attempts = 0
    print("Guess the number between 1 and 100")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Correct! You guessed it in {attempts} attempts.")
            break


# ---------------------------------------------------------------------------
# Lab Exercise 6: Prime number and factorial
# ---------------------------------------------------------------------------
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def lab6_prime_and_factorial():
    num = int(input("Enter a number: "))
    print(num, "is a Prime number" if is_prime(num) else "is not a Prime number")
    if num >= 0:
        print(f"Factorial of {num} is {factorial(num)}")
    else:
        print("Factorial is not defined for negative numbers")


# ---------------------------------------------------------------------------
# Lab Exercise 7: Fibonacci series using recursion
# ---------------------------------------------------------------------------
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def lab7_fibonacci():
    terms = int(input("Enter number of terms: "))
    print("Fibonacci Series:")
    for i in range(terms):
        print(fibonacci(i), end=" ")
    print()
