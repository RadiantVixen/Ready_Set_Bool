

def powerset(a) -> set:
    ps = [[]]

    def rec(subset, i, curr):
        if i >= len(a):
            return
    
        subset.append(a[i])
        ps.append(subset.copy())
        rec(subset, i + 1, curr)


        subset.pop()
        rec(subset, i + 1, curr)



    subset = []
    rec(subset, 0, 0)
    return ps




if __name__  == "__main__":
    print("result =", powerset([0,1,2,3]))


