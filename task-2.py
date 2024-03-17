def maximize_segments(arr, func):
    n = len(arr)
    dp = [0] * n
    prev = [-1] * n

    for i in range(n):
        for j in range(i + 1):
            current_value = func(j, i, arr)
            if j > 0:
                current_value += dp[j - 1]
            if current_value > dp[i]:
                dp[i] = current_value
                prev[i] = j

    segments = []
    i = n - 1
    while i >= 0:
        start = prev[i]
        if start < 0:
            start = 0
        segments.append((start, i))
        i = start - 1
    segments.reverse()

    return dp[-1], segments


def f1(left, right, arr):

    return sum(arr[left:right + 1])


def f2(left, right, arr):
    mod3sum = sum(arr[left:right + 1]) % 3
    if mod3sum == 0:
        return 10
    if mod3sum == 1:
        return 7
    if mod3sum == 2:
        return 2


given_arr = [1, -2, 3, 10, -4, 7, 2, -5]
res_sum, res_segments = maximize_segments(given_arr, f1)
print("f1:  Maximum Sum:", res_sum)
print("f1: Segments:", res_segments)

res_sum, res_segments = maximize_segments(given_arr, f2)
print("f2: Maximum Sum:", res_sum)
print("f2: Segments:", res_segments)
