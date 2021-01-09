def parity(x: int) -> int:
    result = 0
    while x > 0:
        result ^= x & 1
        x >>= 1
    return result
