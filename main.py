"""
FizzBuzz
Fizzbuzz is a commonly overused little toy-program that comes up in entry-level interviews. This is a little test-able spin on it.

Complete the fizzbuzz function that loops over all the numbers from start to end (excluding the end value) and adds them to a list it returns. If the number is a multiple of 3, instead of appending the number, append "fizz". If the number is a multiple of 5, instead append "buzz". If it is a multiple of 3 and 5 then instead append "fizzbuzz".

For example, if start = 1 and end = 8, then the resulting list would contain:

[
    1,
    2,
    "fizz",
    4,
    "buzz",
    "fizz",
    7,
]

"""

def fizzbuzz(start, end):
    fizzbuzz_list = []
    for i in range(start, end):
        if i % 3 == 0 and i % 5 == 0:
            fizzbuzz_list.append("fizzbuzz")
        elif i % 3 == 0:
            fizzbuzz_list.append("fizz")
        elif i % 5 == 0:
            fizzbuzz_list.append("buzz")
        else:
            fizzbuzz_list.append(i)
    return fizzbuzz_list
