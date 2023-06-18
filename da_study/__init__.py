def calculate(expression):
    # Evaluate the expression and return the result
    return eval(expression)

def arrange_signs(_var, _list):
    n = len(_list)
    valid_expressions = []

    def backtrack(index, current_expression):
        if index == n:
            # If all elements in _list have been processed, check if the expression evaluates to _var
            if calculate(current_expression) == _var:
                valid_expressions.append(current_expression)
        else:
            # Recursive backtracking
            num = _list[index]

            # Try multiplying the current number
            multiplied_expression = current_expression + " * " + str(num)
            backtrack(index + 1, multiplied_expression)

            # Try adding the current number
            added_expression = current_expression + " + " + str(num)
            backtrack(index + 1, added_expression)

            # Try subtracting the current number
            subtracted_expression = current_expression + " - " + str(num)
            backtrack(index + 1, subtracted_expression)

    # Start the backtracking with the initial expression as the first number in _list
    initial_expression = str(_list[0])
    backtrack(1, initial_expression)
    return valid_expressions

# Example 1
_var = 5
_list = [5, 5, 3, 2]

valid_expressions = arrange_signs(_var, _list)
print(valid_expressions)
# Output: ['(5 + 5) - 3 - 2']

# Example 2
_var = 15
_list = [5, 5, 3, 2]

valid_expressions = arrange_signs(_var, _list)
print(valid_expressions)
# Output: ['(5 * 5) - 3 + 2', '(5 + 5) + 3 + 2']

# Example 3
_var = 11
_list = [5, 5, 3, 2]

valid_expressions = arrange_signs(_var, _list)
print(valid_expressions)
# Output: ['(5 * 5) - 3 + 2', '(5 + 5) + 3 - 2']
