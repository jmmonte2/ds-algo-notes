'''
A palindrome is a string that reads the same forward and backward,
for example, radar, toot, and madam
'''

from implement_deque import Deque


def palindrome_checker(some_string):
    char_deque = Deque()

    # iterate through string and add chars to deque
    for char in some_string:
        char_deque.add_rear(char)
    
    chars_match = True

    # this accounts for even and odd size of string
    while char_deque.size() > 1 and chars_match:
        first = char_deque.remove_front()
        second = char_deque.remove_rear()

        # check if chars match
        if first != second:
            chars_match = False
    
    return chars_match


print(palindrome_checker("ba"))

