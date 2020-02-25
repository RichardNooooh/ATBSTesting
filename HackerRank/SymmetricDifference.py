m_size = int(input())
m = set(map(int, input().split()))
n_size = int(input())
n = set(map(int, input().split()))

# not_in_sym_diff = m.intersection(n)
# could_be_in_sym_diff = m.union(n)
#
# sym_diff = sorted(could_be_in_sym_diff.difference(not_in_sym_diff))
sym_diff = m ^ n
for num in sym_diff:
    print(num)