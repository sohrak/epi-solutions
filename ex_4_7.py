def power(x: float, y: int) -> float:
    result: float = 1.0
    if y < 0:
        x = 1 / x
        y = -y

    while y > 0:
        if y & 1 == 1:
            result *= x
        x *= x
        y >>= 1
    
    return result
