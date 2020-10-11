print("FIZZBUZZ")
print("This program is designed to print every number from 1-100. When the program encounters a multiple of 3, it will print Fizz. When it encounters a multiple of 5, it will print Buzz. When there is a multiple of both 3 and 5 it will print FizzBuzz.")
for i in range(1, 101):
    if (i % 3 == 0 and i % 5 == 0):
        print("FizzBuzz")
    elif (i % 3 == 0):
       print ("Fizz")
    elif (i % 5 == 0):
        print("Buzz")
    else:
        print(i) 
