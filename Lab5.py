# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
    result = ""
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                result += "*"
            else:
                result += " "
        if i != n - 1:
            result += "\n"
    return result

# 1
# 12
# 123
# 1234
def number_pattern(n):
    result = ""
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            result += str(j)
        if i != n:
            result += "\n"
    return result

# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Example for n = 4:
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):
    result = ""
    for i in range(n):
        result += " " * (n - i - 1)
        result += "*" * (2 * i + 1)
        if i != n - 1:
            result += "\n"
    return result