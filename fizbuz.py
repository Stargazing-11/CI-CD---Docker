def fizzbuzz(i):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

if __name__ == "__main__":
    number = int(input("Enter the starting number: "))
    fizzbuzz(number)