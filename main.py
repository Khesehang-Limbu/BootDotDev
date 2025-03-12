"""

Return the docuRecursion
Recursion is a famously tricky concept to grasp, but it's honestly quite simple - don't let it intimidate you! A recursive function is just a function that calls itself!

Recursion is the process of defining something in terms of itself.


Example of Recursion
If you thought loops were the only way to iterate over a list, you were wrong! Recursion is fundamental to functional programming because it's how we iterate over lists while avoiding stateful loops. Take a look at this function that sums the numbers in a list:

def sum_nums(nums):
    if len(nums) == 0:
        return 0
    return nums[0] + sum_nums(nums[1:])

print(sum_nums([1, 2, 3, 4, 5]))
# 15

Don't break your brain oment's keyword substrings and the document_map copy.

"""


def factorial_r(x):
    if x == 1:
        return x
    if x == 0:
        return 1
    return x * factorial_r(x-1)
