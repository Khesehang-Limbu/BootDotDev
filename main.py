"""
Challenges
In this chapter we are going to practice applying the skills and concepts we learned while building Fantasy Quest.

Number Sum
Write a function called number_sum(n) that adds up all the numbers from 1 to n. For example:

number_sum(5) -> 1+2+3+4+5 -> 15

number_sum(3) -> 1+2+3 -> 6
"""

def number_sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i

    return sum
