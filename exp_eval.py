from stack_array import Stack

# You do not need to change this class
class PostfixFormatException(Exception):
    pass

def postfix_eval(input_str):
    stack = Stack(len(input_str))   # create stack
    postfix_list = input_str.split(" ")     # reformat string into list
    for item in postfix_list:
        if item == "+" or item == "-" or item == "*" or item == "**" or item == "/":
            try:        # try to pop an operand, raise PostfixFormatException if no operands
                op1 = stack.pop()
                op2 = stack.pop()
            except IndexError:
                raise PostfixFormatException("Insufficient operands")
            # operation conditions
            if item == "+":
                stack.push(op2 + op1)
            elif item == "-":
                stack.push(op2 - op1)
            elif item == "*":
                stack.push(op2 * op1)
            elif item == "**":
                stack.push(op2 ** op1)
            elif item == "/":
                if op1 == "0":
                    raise ValueError
                stack.push(op2 / op1)
        else:
            try:        # try to push operand, raise PostfixFormatException if not a valid operand
                stack.push(float(item))
            except ValueError:
                raise PostfixFormatException("Invalid token")
    if stack.size() > 1:    # if stack has more than one item then too many operands were present
        raise PostfixFormatException("Too many operands")
    return stack.pop()      # return final answer as the last item in stack

def prefix_to_postfix(input_str):
    '''Converts a prefix expression to an equivalent postfix expression
    
    Input argument:  a string containing a prefix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** >> << parentheses ( ) or numbers
    Returns a String containing a postfix expression(tokens are space separated)'''
    stack = Stack(len(input_str))  # create stack
    prefix_list = input_str.split(" ")  # reformat string into list
    for item in prefix_list[::-1]:      # reads list in reverse order
        if item == "+" or item == "-" or item == "*" or item == "**" or item == "/":
            try:        # try to pop an operand, raise PostfixFormatException if no operands
                op1 = stack.pop()
            except IndexError:
                raise PostfixFormatException("Invalid token")
            op2 = stack.pop()
            stack.push("%s %s %s" % (op1, op2, item))
        else:
            try:        # try to push operand, raise PostfixFormatException if not a valid operand
                stack.push(item)
            except ValueError:
                raise PostfixFormatException("Invalid token")
    return stack.pop()

