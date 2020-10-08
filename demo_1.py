"""
Let's come up with a plan for the following problem...
```
We'll say that a positive int divides itself if every digit in the number divides into the number evenly. So for example 128 divides itself since 1, 2, and 8 all divide into 128 evenly.
And we'll say that 0 does not divide into anything evenly, so no number with a 0 digit divides itself.

Write a function to determine if a number divides itself.

[source - https://codingbat.com/prob/p165941]
```
"""

# **Understand**


# **Plan**
# loop through the digits in the number
# use % (modulas) to get the rightmost digit
# use / to discard the rightmost
# if dividing by the single digit leaves a remainder, return False
# also if the digit is a zero, return false

# if the loop exits without returning false, then return true

def divides_self(num):
    # set a temp variable to hold the number
    value = num

    # loop through the digits in the number
    # while the value is not zero
    while value != 0:
        # extract the single digit by modding the value by 10
        digit = int(value % 10)
        print('digit:', digit)

        # check if the digit is zero or if the num mod the digit is not zero
        if digit == 0 or num % digit != 0:
            # return False
            return False

        # divide our value by 10 to make sure we do not get an infinite loop
        value = value // 10

    # return True
    return True

# BELOW WORKS AS WELL
# def divides_self(num):
#     value = [int(x) for x in str(num)]
#     for v in value:
#         if v == 0 or num % v != 0:
#             return False
#     return True

print(divides_self(128)) # -> True
print(divides_self(12)) # -> True
print(divides_self(120)) # -> False