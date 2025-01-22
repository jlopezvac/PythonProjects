def sum_brute_force(N):
    res = 0
    for i in range(1, N+1):
        res +=i
    return res

def sum_formula(N):
    return int(N*(N+1)/2)

res1 = sum_brute_force(50)
res2 = sum_formula(50)

print("by brut {} and by formula {}".format(res1, res2))