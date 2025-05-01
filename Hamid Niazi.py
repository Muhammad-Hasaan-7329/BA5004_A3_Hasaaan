def calculator(a, b, operator):
    """
    Simple calculator function.

    Parameters:
        a (float): First operand.
        b (float): Second operand.
        operator (str): One of '+', '-', '*', '/', '%', '**'.

    Returns:
        float: Result of the operation.

    Raises:
        ValueError: If the operator is invalid or division by zero is attempted.
    """
    import operator as op

    # Map symbols to their corresponding functions
    ops = {
        '+': op.add,
        '-': op.sub,
        '*': op.mul,
        '/': op.truediv,
        '%': op.mod,
        '**': op.pow,
    }

    # Validate operator
    if operator not in ops:
        raise ValueError(f"Unsupported operator '{operator}'. Choose from {', '.join(ops.keys())}.")

    # Prevent division by zero
    if operator == '/' and b == 0:
        raise ValueError("Division by zero is not allowed.")

    # Perform and return the operation
    return ops[operator](a, b)
