# FizzBuzz
numbers = [15, 15, 27, 30, 29, 13, 21, 1, 2, 20, 18, 5, 19, 9, 11, 22, 15, 23, 0, 6, 12, 7, 17, 14, 16, 4, 28, 3, 8, 10]

def fizzBuzz(number):
    if(number % 3 == 0  and number % 5 == 0):
      print("FizzBuzz")
    elif(number % 5 == 0):
      print("Buzz")
    elif(number % 3 == 0):
      print("Fizz")
    else:
      print(number)

for number in numbers:
  fizzBuzz(number)