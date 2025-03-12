"""

Resize Image
Doc2Doc should include a feature for image resizing, allowing users to adjust image dimensions to specified ranges. This ensures that images in documents fit and aren't freakishly large or hilariously small.

Assignment
Complete the new_resizer function using currying. It takes integer inputs max_width and max_height and returns an inner function.
The inner function should take optional integer inputs min_width and min_height — with default values 0 — and return an innermost function.
If min_width is more than max_width or min_height is more than max_height, raise an exception "minimum size cannot exceed maximum size".
The innermost function should take two integer inputs width and height and return two integers.
Use the built-in min and max functions to reduce or increase the width and height as needed, then return the new width and new height.
Example
If our new_resizer function returns a set_min_size function, and set_min_size returns a resize_image function, we would use it like this:

# Step 1: Create the resizer with maximum dimensions
set_min_size = new_resizer(800, 600)

# Step 2: Set the minimum dimensions
resize_image = set_min_size(200, 100)

# Step 3: Resize the image
new_width, new_height = resize_image(1000, 500)

# Step 4: Output the result
print(new_width, new_height)  # Output: 800, 500

# With currying syntax
print(new_resizer(800, 600)(200, 100)(1000, 500))  # Output: (800, 500)

"""


def new_resizer(max_width, max_height):
    def check_minimuns(min_width=0, min_height=0):
        if min_width > max_width or min_height > max_height:
            raise Exception("minimum size cannot exceed maximum size")

        def get_width_height(width, height):
            new_width = width
            new_height = height

            if width > max_width:
                new_width = max_width
            elif width < min_width:
                new_width = min_width

            if height > max_height:
                new_height = max_height
            elif height < min_height:
                new_height = min_height
            return new_width, new_height
        return get_width_height
    return check_minimuns

