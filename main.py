"""
Double the String!
The fantasy quest team wants to add a new easter egg potion to Fantasy Quest! It causes characters to have their in-game chat manipulated when they send messages. The potion doubles every character they send!

The message they type: Hello there
The message that is sent: HHeelllloo  tthheerree
Assignment
Complete the double_string function. It takes a string as input and returns a "doubled" version, including spaces!

Example output

sentence = "LF3M BRD full clear"
print(double_string(sentence)) # "LLFF33MM  BBRRDD  ffuullll  cclleeaarr"
"""

def double_string(string):
    double_string = ""
    for char in string:
        double_string += char + char
    return double_string


