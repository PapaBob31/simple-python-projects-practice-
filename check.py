"""A python function that returns the highest no from a series of numbers"""
def mymax(*nos):
    if len(nos) == 1:
        if isinstance(nos[0], list):
            no_list = nos[0]
            max_no = no_list[0]
            for no in no_list[1:]:
                if max_no >= no:
                    max_no = max_no
                else:
                    max_no = no
    elif len(nos) > 1:
        max_no = nos[0]
        for no in nos[1:]:
            if max_no >= no:
                max_no = max_no
            else:
                max_no = no
    return max_no

# Surely there must be a better way


"""A python function that returns 1 if the string passed has well formatted brackets
and returns 0 if the string's brackets are not well formatted or it has no brackets at all
e.g '(a (boy))' returns 1 and '(a (boy)' or 'a boy'returns 0"""

def checkbrackets(text):
    # stores the first_half of the brackets '('
    first_halves = []
    # stores the second_half of the brackets ')'
    second_halves = []
    
    # if brackets are contained in the string
    if "(" in text or ")" in text:
        for char in text:
            if char == "(":
                first_halves.append(char)
            elif char == ")":
                second_halves.append(char)
                if first_halves:
                    first_halves.remove(first_halves[-1])
                    second_halves.remove(second_halves[0])
        # if at the end of the loop, both lists are empty, return 1
        if not first_halves and not second_halves:
            return 1
        else:
            return 0
    else:
        return 0 

# Surely there must be a better way
x = 'a', 'b'; y = 2
print(x, y)
