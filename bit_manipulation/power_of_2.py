# Power of Two – Explanation

# Problem Statement
# Given an integer n, determine if it is a power of two.
# A number is a power of two if it can be expressed as 2^x, where x is a non-negative integer (0,1,2,...).

# Examples
# ✅ n = 1 → True (since 2⁰ = 1)
# ✅ n = 2 → True (since 2¹ = 2)
# ✅ n = 16 → True (since 2⁴ = 16)
# ❌ n = 18 → False (since 18 is not a power of two)


def is_power_of_two(n):
    print(bin(n)[2:])
    print(bin(n - 1)[2:])
    # comparing with & operator
    return n > 0 and (n & (n - 1)) == 0

print(is_power_of_two(1))   # True
print(is_power_of_two(2))   # True
print(is_power_of_two(16))  # True
print(is_power_of_two(18))  # False
print(is_power_of_two(0))  # False
