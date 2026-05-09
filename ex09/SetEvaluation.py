from collections import defaultdict


def  eval_formula(s, set_map, universe):
    if not s:
        return False

    stack = []
    for c in s:
        if c.isalpha():
            stack.append(set_map[c])
        elif c == '!':
            if len(stack) < 1:
                print("the formula is invalid")
                return False
            A = stack.pop()
            stack.append(universe - A)
        else:
            if len(stack) < 2:
                print("the formula is invalid")
                return False
            A = stack.pop()
            B = stack.pop()
            if c == '&':
                stack.append(A & B)
            elif c == '|':
                stack.append(A | B)
            elif c == '^':
                stack.append(A ^ B)
            elif c == '>':
                stack.append((universe - A) | B)
            elif c == '=':
                stack.append((A & B) | ((universe - A) & (universe - B)))
            else:
                print("the formula is invalid")
                return False
    
    if len(stack) > 1:
        print("the formula is invalid")
        return False
    return stack[0]


def eval_set(s, sets):
    set_map = defaultdict(int)
    i = 0
    universe = set().union(*sets)

    for c in s:
        if c.isalpha() and c not in set_map:
            if i >= len(sets):
                print("invalid input")
                return
            set_map[c] = sets[i]
            i += 1
    return eval_formula(s, set_map, universe)

if __name__ == "__main__":

    sets = [
        {0, 1, 2},
        {0, 3, 4},
    ]

    result = eval_set("AB&", sets)
    # [0]
    print(result)

    sets = [
        {0, 1, 2},
        {3, 4, 5},
    ]

    result = eval_set("AB|", sets)
    # [0, 1, 2, 3, 4, 5]
    print(result)

    sets = [
        {0, 1, 2},
    ]

    result = eval_set("A!", sets)
    # []
    print(result)