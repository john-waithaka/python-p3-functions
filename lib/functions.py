#!/usr/bin/env python3

# test 1
# function greetProgrammer() {
#   console.log("Hello, programmer!");
# }

def greet_programmer():
    print("Hello, programmer!")

# test 2
# function greet(name) {
#   console.log(`Hello, ${name}!`);
# }

def greet(name = "John"):
    print(f"Hello, {name}!")

# test 3 and 4
#   You should be able to call this function with no arguments and see its output in the terminal:
#   greetWithDefault();
#   => "Hello, programmer!"

#   You should also be able to call this function with one argument and see its output in the terminal:
#   greetWithDefault("Sunny");
#   => "Hello, Sunny!"
# 
# function greetWithDefault(name = "programmer") {
#   console.log(`Hello, ${name}!`);
# }

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

greet_with_default()

greet_with_default("Sunny")


# test 4      
# /*
#   You should be able to call this function with two arguments and get back its return value:
#   const sum = add(1, 2);
#   console.log(sum);
#   => 3
# */
# def add(num1, num2):
#     pass

def add(num1, num2):
 
    return num1 + num2

# Call the function with arguments and print the result
sum_result = add(1, 2)
print(sum_result)



# last test
def halve(number):
    pass


def halve(number):
  """Halves a number if it's a number, otherwise returns None."""
  if not isinstance(number, (int, float)):  # Check for both int and float
    return None
  return number / 2

# Call the function with a number and print the result
result = halve(4)
print(result)  # Output: 2.0

# Call the function with a non-numeric argument and print the result
result = halve("two")
print(result)  # Output: None

