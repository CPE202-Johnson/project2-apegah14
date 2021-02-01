from stack_array import Stack

# You do not need to change this class
class PostfixFormatException(Exception):
    pass

# string -> float
# takes in a postfix string and calculates the results, raises format exceptions and errors if input is incorrect
def postfix_eval(input_str):
    stack = Stack(len(input_str))   # create stack
    postfix_list = input_str.split(" ")     # reformat string into list
    for item in postfix_list:
        if item == "+" or item == "-" or item == "*" or item == "**" or item == "/":
            try:        # try to pop an operand, raise PostfixFormatException if no operands
                op2 = stack.pop()
                op1 = stack.pop()
            except IndexError:
                raise PostfixFormatException("Insufficient operands")
            # operation conditions
            if item == "+":
                stack.push(op1 + op2)
            elif item == "-":
                stack.push(op1 - op2)
            elif item == "*":
                stack.push(op1 * op2)
            elif item == "**":
                stack.push(op1 ** op2)
            elif item == "/":
                if op2 == 0:
                    raise ValueError
                stack.push(op1 / op2)
        else:
            try:        # try to push operand, raise PostfixFormatException if not a valid operand
                stack.push(float(item))
            except ValueError:
                raise PostfixFormatException("Invalid token")
    if stack.size() > 1:    # if stack has more than one item then too many operands were present
        raise PostfixFormatException("Too many operands")
    return stack.pop()      # return final answer as the last item in stack

# string -> string
# takes in a prefix string and converts it to postfix, raises format exceptions and errors if input is incorrect
def prefix_to_postfix(input_str):
    stack = Stack(len(input_str))  # create stack
    prefix_list = input_str.split(" ")  # reformat string into list
    for item in prefix_list[::-1]:      # reads list in reverse order
        if item == "+" or item == "-" or item == "*" or item == "**" or item == "/":
            op1 = stack.pop()
            op2 = stack.pop()
            stack.push("%s %s %s" % (op1, op2, item))
        else:
            stack.push(item)
    return stack.pop()