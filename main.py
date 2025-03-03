"""
Area Sum
Complete the area_sum() function. It accepts a list of rectangles, where each rectangle is a dictionary that has the following structure:

{
  "height": 5,
  "width": 6
}

The function will calculate the area of each rectangle, then sum them all up and return the result.
"""

def area_sum(rectangles):
    sum = 0
    for rectangle in rectangles:
        area = rectangle["height"] * rectangle["width"]
        sum += area
    return sum

