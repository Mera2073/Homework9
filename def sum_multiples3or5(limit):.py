def sum_multiples3or5(limit):
    total = 0
    for num in range(limit):
        if num % 3 == 0 or num % 5 == 0:
            total += num
    return total

limit = 1000
result = sum_multiples3or5(limit)
print("The sum of all multiples of 3 or 5 below", limit, "is:", result)