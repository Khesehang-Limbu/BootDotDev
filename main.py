"""
Total Score
The recently added Fantasy Quest battlegrounds are having issues with their in-game score due to how the data is being stored. The first-half score and second-half score are stored in separate dictionaries, making it difficult for them to parse the overall score. You've been asked to write a function that merges the two dictionaries and another function that calculates the total score.

Assignment
Complete the merge and total_score functions.

merge
Complete the merge function. It accepts two score dictionaries as input and returns a single merged dictionary that contains all the keys and values from the input dictionaries.

If a key exists in both dictionaries, the value from the second dictionary should overwrite the value from the first dictionary. Here is an example of how the merge function should work after you have implemented it correctly:

two_towers = {"Frodo": "One Ring", "Aragorn": "Narsil"}
rotk = {"Aragorn": "Andúril", "Gandalf": "Glamdring"}
merged_dict = merge(two_towers, rotk)
print(merged_dict)
# {'Frodo': 'One Ring', 'Aragorn': 'Andúril', 'Gandalf': 'Glamdring'}

Notice how the key Aragorn's value gets overridden. His sword got upgraded.

You must implement the merge function, it is not provided for you. If you try calling merge inside the function definition, you will run into problems.

total_score
This function should take a single score dictionary as input and return the total score calculated from the values of that dictionary.

If no points were scored, the function should return 0.

Don't forget: you can always add print() statements to your code so that you can debug your code before submitting! Print out values of variables to see what's going on, and question your assumptions about what you think is happening.

Example of Debugging With Print Statements
def total_score(score_dict):
    print(f"score_dict: {score_dict}")
    for key in score_dict:
        print(f"key: {key}")

You would then run your code and manually inspect the output to see what's going on. You can always remove the print statements when you're done debugging if you want.
"""

def merge(dict1, dict2):
    merged_dict = {}
    for k,v in dict1.items():
        merged_dict[k] = v
        for key,value in dict2.items():
            if k == key:
                merged_dict[k] = value
            else:
                merged_dict[key] = value
    return merged_dict


def total_score(score_dict):
    total = 0
    for k, v in score_dict.items():
        total += v
    return total

