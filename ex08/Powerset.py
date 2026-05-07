

def powerset(a) -> set:
    ps = []

    def rec(subset, curr):
        if curr >= 2 ** len(a):
            return

        for j in range(len(a)):
            subset.append(a[j])
            ps.append(subset.copy())
            curr += 1

        subset.pop()
        rec(subset.copy(), curr+1)
        





    subset = []
    rec(subset, 0)
    return ps




if __name__  == "__main__":
    print("result =", powerset([0,1]))


