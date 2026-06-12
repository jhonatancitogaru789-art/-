def sum_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

print(f"1到100的和是{sum_n(100)}")