from itertools import product

k, m = map(int, input().split())
list_of_k = []
for _ in range(k):
    raw_list = input().split()
    _, cur_list = raw_list[0], map(int, raw_list[1:])
    list_of_k.append(cur_list)

cartesian_product_comb = list(product(*list_of_k))

highest_sum = -1
for comb in cartesian_product_comb:
    cur_sum = 0
    for num in comb:
        cur_sum += num ** 2

    cur_sum %= m
    if cur_sum > highest_sum:
        highest_sum = cur_sum

print(highest_sum)