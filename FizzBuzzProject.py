# def function_here(max_num here)
#     use the for in loop here call the max num in the arguments(you will use range)
#         print that out should print FizzBuzz
#     now use the elif (using modulus operator)
#         print should print Buzz
#     now use another elif (use another modulus operator here)
#         should print fizz
#     lastly using the else:
#         and finally print the num


# simply call the function and pass in the max number

def fizz_buzz(max_num):
  for num in range(1, max_num + 1):
      if num % 3 == 0 and num % 5 == 0:
          print('FizzBuzz')
      elif num % 3 == 0:
            print('Fizz')
      elif num % 5 == 0:
            print('Buzz')
      else:
            print(num)

fizz_buzz(100)

