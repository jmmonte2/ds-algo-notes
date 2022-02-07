'''
Balanced parentheses
means that each opening symbol 
has a corresponding closing symbol and the pairs of
parentheses are properly nested.

Ex:
(()()()())

'''


def bal_parentheses(user_string):
    stack = []
    balanced = True
    index = 0

    # want to iterate through the string
    while index < len(user_string) and balanced:
        some_char = user_string[index]

        # push opens on stack and check if closed matches the open
        if some_char == "(":
            stack.append(some_char)
        else:
            # if stack not empty
            if stack:
                stack.pop()

            # if stack is empty
            else:
                balanced = False

        index = index + 1

    # stack needs to be empty and balanced
    if balanced and not stack:
        return True
    else:
        return False

print(bal_parentheses("()()("))


