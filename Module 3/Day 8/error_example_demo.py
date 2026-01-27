# SyntaxError - Error in the syntax of our code (the way it's written)
# Generally, missing a : or similar
# Your program won't run if there are syntax errors
variable = 1

# SyntaxError: expected ':'
if variable == 1: # as I've left out the : this is a syntax error
    print("Yay!")

# IndentationErrors - This is when your indenting doesn't match
# Your code may run, but bad things happen.
if variable == 1:
    print("Yay!")
    # IndentationError: unexpected indent
     print("IndentationError") # I have an extra space here, so I get an IndentationError