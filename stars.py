# Stars Assignment
# Write the following functions.

# Part I
# Create a function called draw_stars() that takes a list of numbers and prints
# out *.
def draw_stars(numbers):
    for each in range(0, len(numbers)):
        star_string = ""
        for _count in range(0, numbers[each]):
            star_string += '*'
        print star_string

XLIST = [4, 6, 1, 3, 5, 7, 25]
draw_stars(XLIST)

# Part II
# Modify the function above. Allow a list containing integers and strings to be
# passed to the draw_stars() function. When a string is passed, instead of
# displaying *, display the first letter of the string according to the example
# below. You may use the .lower() string method for this part.
def draw_stars_ii(numbers):
    for each in range(0, len(numbers)):
        star_string = ""
        if isinstance(numbers[each], int):
            for _count in range(0, numbers[each]):
                star_string += '*'
        elif isinstance(numbers[each], str):
            for _letter in range(0, len(numbers[each])):
                star_string += numbers[each][0].lower()
        print star_string

YLIST = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars_ii(YLIST)
