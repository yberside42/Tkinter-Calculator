import math 

# === Global State ===
expression = ""
history = []
HISTORY_LIMIT = 5
ALLOWED_OPERATORS = set("+-*/")

# === Funciones ===
def press(num: str | int) -> None:
    """Append a number, decimal point or operator to the current expression.
    
    Args: 
        num (str | int): Digit / Decimal point / Operator pressed.
    """
    global expression
    expression = expression + str(num)
    
def equalpress() -> None:
    """Evaluate the expression and display the result.
    
    Exceptions: 
        ValueError: If invalid characters are detected during evaluation.
    """
    global expression
    allowed_chars = "0123456789+-*/.() "
    if  not all(chars in allowed_chars for chars in expression):
        loghist("ERROR")
        return "ERROR"
            
    try:
        total = str(eval(expression, {"__builtins__": None}, {"math": math}))
        loghist(total)
        expression = ""
        return total
    except Exception:
        loghist("EROR")
        return "ERROR"

def loghist(total: str | int, expr_override: str | None = None) -> None:
    """Save the evaluated expression and the result into the global history.
    
    Args: 
        total(str | int): Result of the evaluated expression.
        expr_override (str | None): Optional expression to log instead of the current one.
    
    Effects: 
        - Appends the expression and the result to the 'history' list.
        - Keeps only the las 5 items; if exceeded the oldest entry is removed
    """
    global expression, history
    expr = expression if expr_override is None else expr_override
    history.append(f"{expr} = {total}")
    if len(history) > HISTORY_LIMIT:
        history.pop(0)
        
def history_text() -> str:
    """Return the history as a printable string."""
    return "\n".join(history)

def clear_history() -> None:
    """Clear the history list."""
    global history
    history = []
    
def clear() -> None:
    """Clear the current expression and add a CLEARED entry to history."""
    global expression
    previous = expression
    expression = ""
    loghist("CLEARED", expr_override=previous)


def press_decimal() -> None:
    """Append a decimal point to the current expression. 
    
    Notes:
        - Prevents adding more than one decimal point within the current number.
        - Inserts '0' if the expression is either empty or ends with an operator.
    """
    global expression
    if not expression:
        expression = "0."
        return
    
    last_char = expression[-1]
    if last_char in ALLOWED_OPERATORS:
        expression += "0."
        return
    
    i = len(expression) - 1
    while i >= 0 and (expression[i].isdigit() or expression[i] == "."):
        i -= 1
    current_token = expression[i + 1:]

    if "." not in current_token and last_char != ".":
        expression += "."
        
def press_back() -> None:
    """Erase the last character from the current expression."""
    global expression
    if len(expression) > 0:
        expression = expression[:-1]
