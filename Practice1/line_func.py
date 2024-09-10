def line_func(x1, y1, x2, y2):
    a = y2 - y1
    b = x1 - x2
    c = a * x1 + b * y1
    
    return f"{a}x + {b}y = {c}"