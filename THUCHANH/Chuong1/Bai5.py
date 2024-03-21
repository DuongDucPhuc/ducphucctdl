def sum_of_divisors(n):
    sum_div = 1 
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            if i == (n // i):
                sum_div += i
            else:
                sum_div += (i + n // i)
    return sum_div
def classify_number(n):
    sum_div = sum_of_divisors(n)
    if sum_div < n:
        return "deficient"
    elif sum_div == n:
        return "perfect"
    else:
        return "abundant"
def print_classification(x, y):
    for num in range(x, y + 1):
        classification = classify_number(num)
        print(f"Số {num} là {classification}")
a= print_classification(6, 8)
print(a)