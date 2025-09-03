# --- Fibonacci Generator ---
def fibonacci(n: int):
    """Return the first n Fibonacci numbers."""
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq[:n]
  
# ---  Prime Checker ---
def is_prime(num: int) -> bool:
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# --- Demo run ---
if __name__ == "__main__":
    print(" First 10 Fibonacci numbers:", fibonacci(10))
    print(" Is 29 prime?", is_prime(29))
